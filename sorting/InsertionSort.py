# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:04
# @Author : yk
# @FileName: InsertionSort.py

'''
当前位置的元素和前一个的元素比较；如果大于，则下一个；如果小于，则继续和前面的元素比较
'''


list = [5, 4, 6, 1, 2, 3, 2]

def insertionSort(list):
    l = len(list)
    for i in range(1, l):
        pre = i-1
        current = list[i]
        while pre >= 0 and list[pre] > current:
            list[pre+1] = list[pre]
            pre -= 1
        list[pre + 1] = current;
    return list

print(insertionSort(list))


