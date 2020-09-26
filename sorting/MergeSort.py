# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:54
# @Author : yk
# @FileName: MergeSort.py

'''
将列表分为两个列表，对这两个列表分别使用归并排序，再把排好序的两个列表合并
'''

list = [5, 4, 6, 1, 2, 3, 2]

def mergeSort(list):
    l = len(list)
    if l < 2: return list
    left = list[:int(l/2)]
    right = list[int(l/2):]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]

    if len(left):
        result += left

    if len(right):
        result += right

    return result

print(mergeSort(list))