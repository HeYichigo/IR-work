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
train_index = train["ID"]
label_index = label["ID"]

train.index = train_index.tolist()
label.index = label_index.tolist()

# train.to_csv("IIID_train.csv")
label.to_csv("IIIID_label.csv")

# result = pd.concat([label, train], axis=0, join='inner')
# result.to_csv("result.csv")
"""
"""
stop_time = time.time()
