from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

""" 试验 joblib保存非神经网络  成功~！"""

vectorizer = joblib.load("vectorizer.pkl")
texts3 = "We 如果 入锅 哈哈哈"
vector2 = vectorizer.transform([texts3])
print("+++++++++++++++")
print(vector2.toarray())
