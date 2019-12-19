import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.externals import joblib
import os
import time
import numpy as np


def tokenizer_space(line):
    # 按空格分词
    return [li for li in line.split() if li.strip() != '']


def get_data_tf_idf(content):
    # 邮件样本已经分好了词，词之间用空格隔开，所以 tokenizer=tokenizer_space
    vectoring = TfidfVectorizer(
        input='content', tokenizer=tokenizer_space, analyzer='word')
    vectorizer = vectoring.fit(content)
    joblib.dump(vectorizer, "train_vectorizer.pkl")
    vector = vectorizer.transform(content)
    vector = vector.todense()
    # print(x, vectoring)
    return vector


start_time = time.time()
emailframe = pd.read_csv("jieba_train.csv")
textmatrix = get_data_tf_idf(emailframe["TEXT"])
stop_time = time.time()
print('totally cost', stop_time-start_time)
