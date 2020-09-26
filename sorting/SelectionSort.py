# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:31
# @Author : yk
# @FileName: SelectionSort.py

'''
将列表分为一个无序区和一个有序区，找到无序区中的最小数放在有序区的末尾
'''

list = [5, 4, 6, 1, 2, 3, 2]

def selectionSort(list):
    l = len(list)
    for i in range(l-1):
        min = i
        for j in range(i+1, l):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
        print(list)
    return list

print(selectionSort(list))