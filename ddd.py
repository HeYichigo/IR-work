import codecs
import pandas as pd
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes as bayes
from sklearn.externals import joblib
# transform text to sparse matrix


def transformTextToSparseMatrix(texts):
    vectorizer = CountVectorizer(binary=False)
    vectorizer.fit(texts)
    joblib.dump(vectorizer, "vectorizer.pkl")
    # inspect vocabulary
    vocabulary = vectorizer.vocabulary_
    print("There are ", len(vocabulary), " word features")

    """
    方案1：测试集和训练集一起进行特征提取
    方案2：测试集用vectorizer.transform()进行特征提取
    目的：测试集和训练集获得相同大小的特征 获得词向量模型 用joblib保存下来
    """

    vector = vectorizer.transform(texts)
    shape = vector.get_shape()[0]
    for col_num in range(0, shape):
        col = vector.getrow(col_num)
        # temp.append(col.toarray()[0])
        result = pd.DataFrame(col.toarray()[0])
        result.to_csv("train_vector.csv", mode="a", header=False, index=False)

    # result = pd.DataFrame(temp)
    # result.to_csv("train_vector.csv")

    keys = []
    values = []
    for key, value in vectorizer.vocabulary_.items():
        keys.append(key)
        values.append(value)
    df = pd.DataFrame(data={"key": keys, "value": values})
    df.to_csv("vocabulary.csv")
    colnames = df.sort_values("value")["key"].values
    result.columns = colnames
    return result


start_time = time.time()
emailframe = pd.read_csv("jieba_train.csv")
textmatrix = transformTextToSparseMatrix(emailframe["TEXT"])

features = pd.DataFrame(textmatrix.apply(sum, axis=0))
extractedfeatures = [features.index[i]
                     for i in range(features.shape[0]) if features.iloc[i, 0] > 5]
textmatrix = textmatrix[extractedfeatures]
print("There are ", textmatrix.shape[1], " word features")

train, test, trainlabel, testlabel = train_test_split(
    textmatrix, emailframe["TYPE"], test_size=0.2)
# train model
clf = bayes.BernoulliNB(alpha=1, binarize=True)
model = clf.fit(train, trainlabel)
# model score
model.score(test, testlabel)

stop_time = time.time()
print('totally cost', stop_time-start_time)
