from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

from sklearn.externals import joblib

csv = pd.read_csv("train_vector.csv")
texts1 = "We 如果 我 是 一只 鸟"
texts2 = "We 如果 我 不是 你 的 话"
texts3 = "We 如果 入锅 哈哈哈"
texts1 = [texts1, texts2]
train_set = [tmp.lower() for tmp in texts1]
vectorizer = CountVectorizer(binary=False)
vectorizer.fit(train_set)

# inspect vocabulary
vocabulary = vectorizer.vocabulary_
print("There are ", len(vocabulary), " word features")
"""
    方案1：测试集和训练集一起进行特征提取
    方案2：测试集用vectorizer.transform()进行特征提取
    目的：测试集和训练集获得相同大小的特征
"""
joblib.dump(vectorizer, "vectorizer.pkl")
temp = []
vector = vectorizer.transform(train_set)
shape = vector.get_shape()[0]
for col_num in range(0, shape):
    col = vector.getrow(col_num)
    temp.append(col.toarray()[0])
print(temp)
temp = pd.DataFrame(temp)
temp.to_csv("尝试.csv")
print("++++++++++++++")
vector1 = vectorizer.transform(train_set)
vector2 = vectorizer.transform([texts3])

print(vector1.tobsr())
print("+++++++++++++++")
print(vector2.toarray())
