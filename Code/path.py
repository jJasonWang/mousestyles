def path(movement, stop_threshold, min_path_length):
    """
    Return a list object of path indices for specific
    movement. Each element in the list is a list containing
    two indices. The first element is start index and the 
    second element is end index.
    ----------
    movement : pandas.DataFrame
        CT, CX, CY coordinates and home base status
        of the combination of strain, mouse and day
    stop_threshold : int
        positive integer indicating the stopping criteria
    min_path_length : int
        positive integer indicating the minimum length of 
        paths
    Returns
    -------
    paths index : a list containing the indices for all paths 
    Examples
    --------
    >>> movement = load_movement(1, 2, 1)
    >>> paths = path(movement, 1, 1)
    """

    T = movement['t'].ravel()
    # Time differences
    TD = np.diff(T)
    path = []
    
    # index
    i = 0
    while i < len(TD):
        start_index = i
        # If time difference is less than threshold, start track the index
        while TD[i] < stop_threshold:
            i += 1
            if TD[i] == len(TD): break
        end_index = i
        
        # Check whether start index is equal to end index
        # If they are equal jump to next index
        if start_index == end_index: next
        else:
            path.append([start_index, end_index])
        
        i += 1
    path = [p for p in path if (p[1] - p[0]) > min_path_length]
    
    return(path)