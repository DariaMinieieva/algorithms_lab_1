'''
This module implements sorting algorithm:
selection sort, insertion sort, merge sort,
shell sort
'''
from random import shuffle


def selection_sort(lst: list) -> int:
    '''
    Selection sort implementation
    '''
    length = len(lst)
    compare = 0

    for i in range(length):
        min_indx = i
        for j in range(i+1, length):
            compare += 1
            if (lst[j] < lst[min_indx]):
                min_indx = j

        lst[i], lst[min_indx] = lst[min_indx], lst[i]

    return compare


def insertion_sort(lst: list) -> int:
    '''
    Insertion sort implementation
    '''
    length = len(lst)
    compare = 1

    for i in range(length):
        j = i

        compare += 1
        while (j > 0) and (lst[j] < lst[j-1]):
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1

    return compare


def merge_sort(lst: list) -> int:
    '''
    Merge sort implementation
    '''
    length = len(lst)
    compare = 0

    if (length > 1):
        mid = length//2

        left = lst[:mid]
        right = lst[mid:]

        first = merge_sort(left)
        second = merge_sort(right)

        compare += (first + second)

        i = j = k = 0

        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            compare += 1

        while (i < len(left)):
            lst[k] = left[i]
            i += 1
            k += 1

        while (j < len(right)):
            lst[k] = right[j]
            j += 1
            k += 1

    return compare


def shell_sort(lst: list) -> int:
    '''
    Shell sort implementation
    '''
    length = len(lst)
    h = 1
    compare = 0

    while (h < (length//3)):
        h = 3*h + 1

    while (h >= 1):
        for i in range(h, length):
            for j in range(i, h-1, -h):
                compare += 1
                if (lst[j] < lst[j-h]):
                    lst[j], lst[j-h] = lst[j-h], lst[j]
                else:
                    break

        h = h//3

    return compare
