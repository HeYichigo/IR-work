import re
import jieba
import codecs
import os
import time

"""
处理邮件数据集
将其处理为.csv格式，便于后续读取
"""

# 去掉非中文字符


def clean_str(string):
    # string = re.sub(r"[^\u4e00-\u9fff]", " ", string)
    # string = re.sub(r"\s{2,}", " ", string)
    string = string.replace("\n", "").replace(
        "\t", "").replace("\r", "").replace(",", " ")
    return string.strip()


def get_data_in_a_file(original_path, save_path='all_email.txt'):
    files = os.listdir(original_path)
    for file in files:
        if os.path.isdir(original_path + '/' + file):
            get_data_in_a_file(original_path + '/' + file, save_path=save_path)
        else:
            email = ''
            # 注意要用 'ignore'，不然会报错
            f = codecs.open(original_path + '/' + file,
                            'r', 'gbk', errors='ignore')
            # lines = f.readlines()
            for line in f:
                line = clean_str(line)
                email += line
            f.close()
            """
            发现在递归过程中使用 'a' 模式一个个写入文件比 在递归完后一次性用 'w' 模式写入文件快很多
            """
            f = open(save_path, 'a', encoding='utf8')
            # email_jieba = [word for word in jieba.cut(
            #     email) if word.strip() != '']
            # f.write(' '.join(email) + '\n')
            f.write(email[12:26]+","+email+"\n")
            print(email[12:26], end="\r")


time_start = time.time()
print('Storing emails in a file ...')
get_data_in_a_file('垃圾邮件分类任务语料\\train\\Data',
                   save_path='train_email.csv')
print('Store emails finished !')
time_end = time.time()
print('totally cost', time_end-time_start)
