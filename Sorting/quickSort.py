__author__ = 'Andy'

import random


def quickSort(list):
    if len(list) == 0: return []
    index = random.randint(0, len(list) - 1)
    left, right, pivot = [], [], list.pop(index)
    for x in list:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quickSort(left) + [pivot] + quickSort(right)