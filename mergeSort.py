__author__ = 'Andy'


def mergeSort(list):
    if (len(list) > 1):
        midpoint = len(list) // 2
        leftlist = list[:midpoint]
        rightlist = list[midpoint:]

        mergeSort(leftlist)
        mergeSort(rightlist)

        i, j, k = (0, 0, 0)

        while (i < len(leftlist) and j < len(rightlist)):
            if (leftlist[i] < rightlist[j]):
                list[k] = leftlist[i]
                i = i + 1
            else:
                list[k] = rightlist[j]
                j = j + 1
            k = k + 1

        while (i < len(leftlist)):
            list[k] = leftlist[i]
            i = i + 1
            k = k + 1
        while (j < len(rightlist)):
            list[k] = rightlist[j]
            j = j + 1
            k = k + 1
    return list