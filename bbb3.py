# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import time
"""
将邮件与label左联，去除缺失的数据集
"""
start_time = time.time()
"""
"""
train = pd.read_csv("train_email.csv")
label = pd.read_csv("re_index.csv")

result = pd.concat([label, train], axis=1, join='inner')

result = result[['ID', 'TYPE', 'TEXT']]
result.to_csv("result.csv", index=False)
"""
"""
stop_time = time.time()
print('totally cost', stop_time-start_time)
