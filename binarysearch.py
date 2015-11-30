__author__ = 'Andy'


def binarySearch(list, val, min=0, maxlen=0):
    if maxlen == 0:
        if val == list[0]: return 0
        maxlen = len(list)
    if maxlen - min > 1:
        mid = (maxlen + min) // 2
        midval = list[mid]
        if val == midval:
            return mid
        elif val < midval:
            return binarySearch(list, val, min, mid)
        else:
            return binarySearch(list, val, mid, maxlen)
    return False


list = [0, 8, 9, 10, 12, 13, 15, 17, 20, 45, 74, 234, 574, 2658, 3414]
print(binarySearch(list, 20))
