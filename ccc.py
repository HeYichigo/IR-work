# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

label_txt = np.loadtxt("label.txt", dtype=int)
DF_label_txt = pd.DataFrame(label_txt)

f = open('all_email.txt', 'r', encoding='utf-8')
sourceInLine = f.readlines()
all_email_txt = []
for line in sourceInLine:
    temp1 = line.strip('\n')
    # temp2 = temp1.split('\n')
    all_email_txt.append(temp1)

DF_all_email = pd.DataFrame(all_email_txt)

DF_full_email_label = pd.concat([DF_label_txt, DF_all_email], axis=1)
# DF_full_email_label = pd.DataFrame.from_dict(DF_label_txt, orient='index')
DF_full_email_label.columns = ['type', 'text']
DF_full_email_label.to_csv("full_email_label.csv")
