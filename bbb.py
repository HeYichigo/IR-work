import time

"""
暂时没有用
"""


def get_label_in_a_file(original_path, save_path='label.txt'):
    f = open(original_path, 'r')
    label_list = []
    for line in f:
        # spam
        if line[0] == 's':
            label_list.append("spam")
        # ham
        elif line[0] == 'h':
            label_list.append("ham")

    f = open(save_path, 'w', encoding='utf8')
    f.write('\n'.join(label_list))
    f.close()


time_start = time.time()
print('Storing labels in a file ...')
get_label_in_a_file('垃圾邮件分类任务语料\index.txt', save_path='label.txt')
print('Store labels finished !')
time_end = time.time()
print('totally cost', time_end-time_start)
