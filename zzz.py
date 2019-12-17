import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import svm, ensemble
from sklearn import naive_bayes as bayes
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.externals import joblib
import os
import numpy as np


def tokenizer_jieba(line):
    # 结巴分词
    return [li for li in jieba.cut(line) if li.strip() != '']


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


def get_label_list(label_file_name):
    f = open(label_file_name, 'r')
    sourceInLine = f.readlines()
    dataset = []
    for line in sourceInLine:
        temp1 = line.strip('\n')
        # temp2 = temp1.split('\n')
        dataset.append(temp1)
    for i in range(0, len(dataset)):
        dataset[i] = int(dataset[i])
    # print(dataset)
    return dataset


def writinfile(ffile=501, cfile=1, path="../Data/"):
    if cfile <= 9:
        return path + str(ffile) + "/00" + str(cfile)
    if cfile > 9 and cfile <= 99:
        return path + str(ffile) + "/0" + str(cfile)
    if cfile >= 100:
        return path + str(ffile) + "/" + str(cfile)


if __name__ == "__main__":
    np.random.seed(1)
    email_file_name = 'all_email.txt'
    label_file_name = 'label.txt'
    x, vectoring = get_data_tf_idf(email_file_name)
    y = get_label_list(label_file_name)

    # x = np.array(x)
    # y = np.array(y)
    # print('x.shape : ', x.shape)
    # print('y.shape : ', y.shape)

    # x = x.tolist()
    # y = y.tolist()
    # 随机打乱所有样本
    index = np.arange(len(y))
    np.random.shuffle(index)
    x = x[index]
    y = np.array(y)[index]

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # clf = bayes.BernoulliNB()
    # clf = svm.LinearSVC()
    # clf = LogisticRegression()
    clf = ensemble.RandomForestClassifier()
    clf.fit(x_train, y_train)
    # clf.fit(x, y)
    """
    保存模型
    """
    # dirs = "model"
    # joblib.dump(clf, dirs+'/clf.pkl')

    """
    下面是预测步骤
    """

    x_out_test, vectoring = get_data_tf_idf("test_email.txt")
    # index = np.arange(x_out_test.shape[0])
    # np.random.shuffle(index)
    # x_out_test = x_out_test[index]
    # y = np.array(y)[index]

    # content = open("test_email.txt", 'r', encoding='utf8').readlines()
    # x_out_test = vectoring.fit_transform(content)
    y_pred = clf.predict(x_test)

    # 输出到文件
    ffile = 501
    cfile = 1
    result_list = [["TYPE", "ID"]]
    result = []
    for line in y_pred[0:10000]:
        if line == 1:
            result = ["ham", writinfile(ffile, cfile)]
        elif line == 0:
            result = ["spam", writinfile(ffile, cfile)]
        result_list.append(result)
        cfile = cfile + 1
        if cfile == 101:
            ffile = ffile + 1
            cfile = 1
    f = open("pred.txt", 'w', encoding='utf8')

    temp = [' '.join(x if x else ' ') for x in result_list]
    f.write('\n'.join(temp))
    f.close()
    ####
    print('classification_report\n',
          metrics.classification_report(y_test, y_pred, digits=4))
    print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
