from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pandas as pd

from mousestyles.path_diversity import compute_angles


def detect_noise(movement, paths, angle_threshold, delta_t):
    r"""
    Return a list object containing boolean values at points
    where measurement noise is detected and will be passed to
    a smoothing function

    Parameters
    ----------
    movement : pandas.DataFrame
        CT, CX, CY coordinates and homebase status
        for the unique combination of strain, mouse and day

    paths index : a list containing the indices for all paths

    angle_threshold : float
        positive number indicating the minimum turning angle to flag as noise

    delta_t : float
        positive number indicating the delta_time interval

    Returns
    -------
    noise index : a pandas series containing the indices at which
    noise, as defined by input parameters, is detected

    Examples
    --------
    >>> movement = data.load_movement(1, 2, 1)
    >>> paths = path_diversity.path_index(movement, 1, 1)
    >>> noise = detect_noise(movement, paths, 135, .1)
    """

    # check if all inputs are positive
    conditions_value = [angle_threshold <= 0, delta_t <= 0]
    if any(conditions_value):
        raise ValueError("Input values need to be positive")

    if not isinstance(movement, pd.core.frame.DataFrame):
        raise TypeError("Movement must be pandas DataFrame")

    if set(movement.keys()) != {'isHB', 't', 'x', 'y'}:
        raise ValueError(
            "The keys of movement must be 't', 'x', 'y', and 'isHB'")

    if len(movement) <= 1:
        raise ValueError("Movement must contain at least 2 rows")

    noise_index = 1
    noise_path = []
    noise_path = pd.Series(noise_path)
    current_noise = False

    for path in paths:
        path_obj = movement[path[0]:path[1] + 1]

        if len(path_obj) > 3:

            path_obj['angles'] = compute_angles(path_obj, False)
            path_obj['sharp_angle'] = path_obj['angles'] > angle_threshold
            path_obj['noise'] = 0

            # Note: The above DataFrame manipulations result in a
            # SettingWithCopyWarning. The warning persists even after
            # attempting the following format:
            # .loc[row_indexer,col_indexer] = value. Despite this,
            # the output of the function is working as intended.

            for i in range(0, len(path_obj) - 1):
                if path_obj['sharp_angle'].iloc[i]:
                    if path_obj['sharp_angle'].iloc[i + 1]:
                        if path_obj['t'].iloc[
                                i + 1] - path_obj['t'].iloc[i] < delta_t:
                            path_obj['noise'].iloc[i] = noise_index
                            path_obj['noise'].iloc[i + 1] = noise_index
                            current_noise = True
                        elif current_noise:
                            noise_index += 1
                            current_noise = False
                    elif current_noise:
                        noise_index += 1
                        current_noise = False
        else:
            path_obj['noise'] = 0

        noise_path = noise_path.append(path_obj.noise)

    return noise_path
