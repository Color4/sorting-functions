# quick sort and bubble sort implementation hw
# jan 2018
# author <christa.caggiano@ucsf.edu>

conditional = 0
assignments = 0


def bubble_sort(l):
    """
    :param l: unsorted list
    :return: sorted list

    keeping track of whether the list is sorted,
    iterate over the list. If the ith index is less than
    the ith + 1 index, swap them. Continue until you make
    no swaps. Return list.

    """
    global conditional
    global assignments

    not_sorted = True  # start with list unsorted
    assignments += 1

    while not_sorted:
        conditional += 1

        not_sorted = False
        assignments += 1

        for i in range(len(l)-1):
            assignments += 1
            conditional += 1
            if l[i] > l[i+1]:

                l[i+1], l[i] = l[i], l[i+1]  # pythonic swap !
                not_sorted = True  # if a swap occurs, list is unsorted
                assignments += 4

    return l


def bubblesort_count(l):
    """
    :param l: list to be sorted
    :return: number of conditionals and number of assignments
    """
    global conditional
    global assignments

    conditional = 0
    assignments = 0

    bubble_sort(l)

    return conditional, assignments

