# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:21:12 2021

@author: jiyem
"""

# integrand function
def f_of_x(x):
    """
    This is the main function we want to integrate over.
    Args:
    - x (float) : input to function; must be in radians
    Return:
    - output of function f(x) (float)
    """
    return (e**(-1*x))/(1+(x-1)**2)
