__author__ = 'Andy'

import timeit

import mergeSort
import quickSort

list = [34, 7, 3, 31, 6, 8, 56, 24, 658, 9, 363, 563, 767, 34, 78, 2, 0, 1, 94]
print("mergeSort: ", mergeSort.mergeSort(list))

print(timeit.timeit('mergeSort.mergeSort(list)',
                    setup='import mergeSort;list = [34, 7, 3, 31, 6, 8, 56, 24, 658, 9, 363, 563, 767, 34, 78, 2, 0, 1, 94]',
                    number=30))

list = [34, 7, 3, 31, 6, 8, 56, 24, 658, 9, 363, 563, 767, 34, 78, 2, 0, 1, 94]
print("quickSort: ", quickSort.quickSort(list))

print(timeit.timeit('quickSort.quickSort(list)',
                    setup='import quickSort;list = [34, 7, 3, 31, 6, 8, 56, 24, 658, 9, 363, 563, 767, 34, 78, 2, 0, 1, 94]',
                    number=30))
