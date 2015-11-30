__author__ = 'Andy'


def quickSort(list):
    if (len(list) == 0): return []
    left, right, pivot = [], [], list[0]
    for i, x in enumerate(list):
        if (i != 0):
            if (x < pivot):
                left.append(x)
            else:
                right.append(x)
    return quickSort(left) + [pivot] + quickSort(right)