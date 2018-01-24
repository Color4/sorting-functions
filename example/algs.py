# quick sort and bubble sort implementation hw
# jan 2018
# author <christa.caggiano@ucsf.edu>

import random


def bubble_sort(l):
    """
    :param l: unsorted list
    :return: sorted list

    keeping track of whether the list is sorted,
    iterate over the list. If the ith index is less than
    the ith + 1 index, swap them. Continue until you make
    no swaps. Return list.

    """
    not_sorted = True # start with list unsorted
    while not_sorted:
        not_sorted = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i+1], l[i] = l[i], l[i+1]  # pythonic swap !
                not_sorted = True  # if a swap occurs, list is unsorted
    return l

def quick_sort(l):
    """
    :param l: unsorted list
    :return: sorted list

    pick a random pivot. Put all the items in the list that
    are less than the pivot in a 'less than list' or greater than in a
    'greater than' list. Recursively call quick_sort on these two lists
    so that a new pivot is chosen each time, sorting smaller and smaller lists
    until the sorted list is returned.
    """

    if len(l) == 0 or len(l) == 1:  # base case, where list is empty or 1 item
        return l

    pivot = random.randint(0, len(l)-1)  # pick random pivot

    # initialize lists for sorting
    less_than = []
    greater_than = []

    # for each index in l, if the index isn't the pivot,
    # add to appropriate list
    for index, item in enumerate(l):
        if not index == pivot:
            if item < l[pivot]:
                less_than.append(item)
            else:
                greater_than.append(item)

    # recursively call the sorting function until a sorted list is returned
    return quick_sort(less_than) + [l[pivot]] + quick_sort(greater_than)

