import codecs
import pandas as pd
import os
import jieba

stopwords = codecs.open('stopwords.txt', 'r', 'UTF8').read().split('\r\n')
emailframe = pd.read_csv("result.csv")
# cut words and process text
processed_texts = []
for text in emailframe["TEXT"]:
    words = []
    seg_list = jieba.cut(text)
    for seg in seg_list:
        if (seg.isalpha()) & (seg not in stopwords):
            words.append(seg)
    sentence = " ".join(words)
    processed_texts.append(sentence)

emailframe["TEXT"] = processed_texts

emailframe.to_csv("jieba_train.csv")
