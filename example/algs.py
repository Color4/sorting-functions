import numpy as np
import random

def bubble_sort(l):
    """
    Describe how you are sorting `x`
    """
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i+1], l[i] = l[i], l[i+1]
                not_sorted = True
    return l

def quick_sort(l):
    """
    Describe how you are sorting `x`
    """
    if len(l) == 0 or len(l) == 1:
        return l
    pivot = random.randint(0, len(l)-1)
    less_than = []
    greater_than = []

    for index, item in enumerate(l):
        if not index == pivot:
            if item < l[pivot]:
                less_than.append(item)
            else:
                greater_than.append(item)
    return quick_sort(less_than) + [l[pivot]] + quick_sort(greater_than)
