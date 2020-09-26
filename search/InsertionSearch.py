# -*- coding: utf-8 -*-
# @Time : 2020/9/26 12:36
# @Author : yk
# @FileName: InsertionSearch.py

'''
改进mid值，将比较点改进为自适应选择
'''

list = [1, 2, 3, 4, 5, 6, 7]

def insertionSearch(list, x, low, high):
    mid = low + int((x-list[low])/(list[high]-list[low])*(high-low))
    if x == list[mid]:
        return mid
    elif x > list[mid]:
        return insertionSearch(list, x, mid + 1, high)
    else:
        return insertionSearch(list, x, low, mid - 1)



print(insertionSearch(list, 2, 0, len(list) - 1))



