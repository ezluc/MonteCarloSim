# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:19:57 2021

@author: jiyem
"""

# Importing librarys

# generate a random number
def get_rand_number(min_value, max_value):
    """
    This function gets a random number from a uniform distribution between
    the two input values [min_value, max_value] inclusively
    Args:
    - min_value (float)
    - max_value (float)
    Return:
    - Random number between this range (float)
    """
    range = max_value - min_value
    choice = random.uniform(0,1)
    return min_value + range*choice