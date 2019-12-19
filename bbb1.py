# -*- coding: UTF-8 -*-
import time
import pandas as pd

"""
处理label数据集
"""


def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    sourceInLine = f.readlines()
    dataset = []
    for line in sourceInLine:
        line = line.replace(" ", ",")
        line = line.replace("/", "\\")
        temp1 = line.strip('\n')
        # temp2 = temp1.split('\n')
        dataset.append(temp1)
    return dataset


time_start = time.time()
print('Storing labels in a file ...')
"""
"""
label_txt = read_file("垃圾邮件分类任务语料\index.txt")
f = open("re_index.csv", 'w', encoding='utf8')
f.write('\n'.join(label_txt))
f.close()
"""
"""
print('Store labels finished !')
time_end = time.time()
print('totally cost', time_end-time_start)
