# quick sort and bubble sort implementation hw
# jan 2018
# author <christa.caggiano@ucsf.edu>

import random

conditional = 0
assignments = 0


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
    global conditional
    global assignments

    conditional += 1
    if len(l) == 0 or len(l) == 1:  # base case, where list is empty or 1 item
        return l

    assignments += 3
    pivot = random.randint(0, len(l)-1)  # pick random pivot

    # initialize lists for sorting
    less_than = []
    greater_than = []

    # for each index in l, if the index isn't the pivot,
    # add to appropriate list
    for index, item in enumerate(l):
        assignments += 1
        conditional += 1
        if not index == pivot:
            conditional += 1
            assignments += 1
            if item < l[pivot]:
                less_than.append(item)
            else:
                greater_than.append(item)
    # recursively call the sorting function until a sorted list is returned
    return quick_sort(less_than) + [l[pivot]] + quick_sort(greater_than)


def quicksort_count(l):
    """
    :param l: unsorted list
    :return: number of conditionals and number of assignments
    """
    global conditional
    global assignments

    conditional = 0
    assignments = 0

    quick_sort(l)

    return conditional, assignments


