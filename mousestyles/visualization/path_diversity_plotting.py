import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

from mousestyles.data.utils import (day_to_mouse_average,
    mouse_to_strain_average, total_time_rectangle_bins,
    pull_locom_tseries_subset, split_data_in_half_randomly)

from mousestyles.data import load_movement,load_start_time_end_time
from mousestyles.path_index import path_index

def plot_box(list_of_arrays, title="Box Plot of Distribution"):
    r"""
    Make a box plot of the desired metric (path length, speed, angle, etc)
    per mouse, day or strain. 

    Parameters
    ----------
    list_of_arrays : list
        each element of the list is a numpy array containing data on the
        metric to be plotted per mouse, day, or strain. Data is typically
        generated from another function in the package.
         
    title : str
        desired title of the plot

    Returns
    -------
    box plot : box plot of the desired metric combinations
    """
    if len(list_of_arrays)== 0:
        raise ValueError("List of arrays can not be empty")
    if type(title) != str:
        raise TypeError("Title must be a string")
    if type(list_of_arrays) != list:
        raise TypeError("List of arrays must be a list")
    xlab = list(range(len(list_of_arrays)))
    plt.boxplot(list_of_arrays, labels=xlab)
    plt.title(title)
    plt.show()

def plot_hist(list_of_arrays, title="Histogram of Distribution",
    xlab="X Values", ylab="Y Values", leg=True):
    r"""
    Make a histogram of the desired metric (path length, speed, angle, etc)
    per mouse, day, or strain. 

    Parameters
    ----------
    list_of_arrays : list
        each element of the list is a numpy array containing data on the
        metric to be plotted per mouse, day, or strain. Data typically 
        generated from another function in the package.
         
    title : str
        desired title of the plot
        
    xlab : str
        desired x axis label of the plot
        
    ylab : str
        desired y axis label of the plot
    
    leg : bool
        indicates whether a legend for the plot is desired
        

    Returns
    -------
    hist plot : histogram of the desired metric combinations
    """
    if len(list_of_arrays)==0:
        raise ValueError("List of arrays can not be empty")
    if type(title) != str:
        raise TypeError("Title must be a string")
    if type(xlab) != str:
        raise TypeError("xlab must be a string")
    if type(ylab) != str:
        raise TypeError("ylab must be a string")
    if type(list_of_arrays) != list:
        raise TypeError("List of arrays must be a list")
    if type(leg) != bool:
        raise TypeError("leg must be a boolean")
    lab = list(range(len(list_of_arrays)))
    plt.hist(list_of_arrays, normed=True, label=lab)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    if leg==True:
        plt.legend()
    plt.title(title)
    plt.show()