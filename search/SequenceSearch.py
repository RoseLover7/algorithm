# -*- coding: utf-8 -*-
# @Time : 2020/9/26 12:10
# @Author : yk
# @FileName: SequenceSearch.py

'''
按照列表顺序去查找，找到则返回
'''

list = [5, 4, 6, 1, 2, 3, 2]

def sequenceSearch(list, x, l):
    for i in range(l):
        if (list[i] == x):
            return i;
    return False;

print(sequenceSearch(list, 2, len(list)))
