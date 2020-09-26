# -*- coding: utf-8 -*-
# @Time : 2020/9/26 12:15
# @Author : yk
# @FileName: BinarySearch.py

'''
列表必须是有序的，无序先排序；和中间的数比较大小，等于则返回；大于在后半部分查找；小于在前半部分查找；
'''

list = [1, 2, 3, 4, 5, 6, 7]

def binarySearch(list, x, low, high):
    mid = int((low+high)/2)
    if x == list[mid]:
        return mid
    elif x > list[mid]:
        return binarySearch(list, x, mid+1, high)
    else:
        return binarySearch(list, x, low, mid-1)

print(binarySearch(list, 6, 0, len(list)-1))
