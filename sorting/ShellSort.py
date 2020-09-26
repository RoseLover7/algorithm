# -*- coding: utf-8 -*-
# @Time : 2020/9/26 11:28
# @Author : yk
# @FileName: ShellSort.py

'''
将序列分为若干个子序列，对每个子序列直接插入排序，当增量为1时，直接对整个序列插入排序
'''


list = [5, 4, 6, 1, 2, 3, 2]

def shellSort(list):
    l = len(list)
    increment = int(l/2)
    while increment > 0:
        for i in range(increment, l):
            tmp = list[i]
            j = i
            while j >= increment and list[j-increment] > tmp:
                list[j] = list[j-increment]
                j -= increment
            list[j] = tmp
        increment = int(increment/2)
    return list

print(shellSort(list))