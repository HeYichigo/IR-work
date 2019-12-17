from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import svm, ensemble
from sklearn import naive_bayes as bayes
from sklearn.model_selection import train_test_split
from sklearn import metrics
import sklearn
import os


def tokenizer_space(line):
    # 按空格分词
    return [li for li in line.split() if li.strip() != '']


def get_data_tf_idf(email_file_name):
    # 邮件样本已经分好了词，词之间用空格隔开，所以 tokenizer=tokenizer_space
    vectoring = TfidfVectorizer(
        input='content', tokenizer=tokenizer_space, analyzer='word')
    content = open(email_file_name, 'r', encoding='utf8').readlines()
    x = vectoring.fit_transform(content)
    # print(x, vectoring)
    return x, vectoring


def writinfile(ffile=501, cfile=1, path="../Data/"):
    if cfile <= 9:
        return path + str(ffile) + "/00" + str(cfile)
    if cfile > 9 and cfile <= 99:
        return path + str(ffile) + "/0" + str(cfile)
    if cfile >= 100:
        return path + str(ffile) + "/" + str(cfile)


clf = joblib.load("model\clf.pkl")
x_out_test = clf.
y_pred = clf.predict(x_out_test)
# 输出到文件
ffile = 501
cfile = 1
result_list = []
result = []
for line in y_pred:
    if line == 1:
        result = ["ham", writinfile(ffile, cfile)]
    elif line == 0:
        result = ["spam", writinfile(ffile, cfile)]
    result_list.append(result)
    ffile = ffile + 1
    cfile = cfile + 1
f = open("pred.txt", 'w', encoding='utf8')

temp = [' '.join(x if x else ' ') for x in result_list]
f.write('\n'.join(temp))
f.close()
####
print('classification_report\n',
      metrics.classification_report(y_test, y_pred, digits=4))
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
