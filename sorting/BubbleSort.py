# -*- coding: utf-8 -*-
# @Time : 2020/9/26 9:41
# @Author : yk
# @FileName: BubbleSort.py


'''
小数上浮，大数沉底
'''

list = [5, 4, 6, 1, 2, 3, 2]

def bubbleSort(list):
    l = len(list)
    for i in range(l):
        for j in range(i, l):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
            else:
                pass
    return list


print(bubbleSort(list))