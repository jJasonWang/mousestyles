import matplotlib.pyplot as plt

def plot_path(path_obj, title=None, alpha=None, plot_type=None):
    r"""
    Returs the plot of the path object with the title given.

    Parameters
    ----------
    path_obj : pandas.DataFrame
        CT, CX, CY coordinates and homebase status.

    title : str
        the title of the plot. Default is 'example plot of path'

    alpha : numeric
        graphical parameter which determines strongness of each
        line. Default is 1.

    plot_type : str
        graphical paramter which determines the type of the plot.
        'b' for line and 'o' for poitns. Default is 'b'.

    Returns
    -------
    Drawing the plot of the path.

    Examples
    --------
    >>> movement = data.load_movement(1,2,1)
    >>> sep = path_index(movement, 1, 1)
    >>> path = movement[sep[2][0]:sep[2][1]+1]
    >>> plot_path(path, "example of the path")
    """

    if title == None:
        title = 'example plot of path'
    if alpha == None:
        alpha = 1
    if plot_type == None:
        plot_type = 'b'
        
    plt.plot(path_obj['x'], path_obj['y'], plot_type, alpha = alpha)
    YLower = 0.9; YUpper = 43.5; XUpper = 3.76; XLower = -16.24
    plt.xlabel('x-coordinate')
    plt.xlim(XLower, XUpper)
    plt.ylabel('y-coordinate')
    plt.ylim(YLower, YUpper)
    plt.title(title)

def plot_rectange(limit_points):
    r"""
    Returs the plot of the regtangle spanned by the path.

    Parameters
    ----------
    limit_points : dictionary
        must contain xmax,xmin,ymax,ymin.
        Expecting the output of find_limit_points.

    Returns
    -------
    Drawing the rectangle spanned by the path.

    Examples
    --------
    >>> movement = data.load_movement(1,2,1)
    >>> sep = path_index(movement, 1, 1)
    >>> path = movement[sep[2][0]:sep[2][1]+1]
    >>> plot_path(path, "example of the path")
    >>> limit = find_limit_points(path)
    >>> plot_rectange(limit)
    """

    x_cent, y_cent = find_center(limit_points).values()
    plt.plot(x_cent,y_cent, 'o', c = 'g')
    plt.plot([limit_points['xmin'], limit_points['xmin']], [limit_points['ymin'], limit_points['ymax']],'b', c = 'r')
    plt.plot([limit_points['xmin'], limit_points['xmax']], [limit_points['ymin'], limit_points['ymin']],'b', c = 'r')
    plt.plot([limit_points['xmax'], limit_points['xmax']], [limit_points['ymin'], limit_points['ymax']],'b', c = 'r')
    plt.plot([limit_points['xmin'], limit_points['xmax']], [limit_points['ymax'], limit_points['ymax']],'b', c = 'r')
    plt.plot([limit_points['xmin'], limit_points['xmax']], [limit_points['ymin'], limit_points['ymax']],'b', c = 'r')
    plt.plot([limit_points['xmin'], limit_points['xmax']], [limit_points['ymax'], limit_points['ymin']],'b', c = 'r')

def plot_radius(path_obj, center):
    r"""
    Returs the plot of the radius in the path.
    Radius is defined by the vector connecting the center point of the 
    path and each point of the path.

    Parameters
    ----------
    path_obj : pandas.DataFrame
        CT, CX, CY coordinates and homebase status.

    center : dictionary
        must contain x and y. Expecting the output of find_center.

    Returns
    -------
    Drawing the radius in the path.

    Examples
    --------
    >>> movement = data.load_movement(1,2,1)
    >>> sep = path_index(movement, 1, 1)
    >>> path = movement[sep[2][0]:sep[2][1]+1]
    >>> limit = find_limit_points(path)
    >>> cent = find_center(limits)
    >>> plot_radius(path_ex, cent)
    """


    x_cent, y_cent = center.values()
    plt.plot(x_cent, y_cent, 'o', c = 'g')
    for i in range(len(path_obj)):
        plt.plot([x_cent, path_obj[i:i+1]['x']],[y_cent, path_obj[i:i+1]['y']],'b',c='r')