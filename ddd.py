import codecs
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import naive_bayes as bayes
# transform text to sparse matrix


def transformTextToSparseMatrix(texts):
    vectorizer = CountVectorizer(binary=False)
    vectorizer.fit(texts)

    # inspect vocabulary
    vocabulary = vectorizer.vocabulary_
    print("There are ", len(vocabulary), " word features")

    vector = vectorizer.transform(texts)

    result = pd.DataFrame(vector)
    result.to_csv("vector.csv")

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
