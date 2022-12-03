#!/usr/bin/python3

    """
    Print a list of integers
    ...

    Parameters
    ----------
    my_list : list optional
        The list of integers

    Return:
        None
    """

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
