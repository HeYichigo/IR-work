import pandas as pd
import codecs
emailframe = pd.read_csv("full_email_label.csv")

# DF_full_email_label = DF_full_email_label.dropna(subset=['text'])

emailframe = emailframe.dropna(subset=['text'])

emailframe.to_csv("filter_full_email_label.csv")
emailframe.head(3)

print("data shape:", emailframe.shape)
# 0 = spams 1 = ham
print("spams in rows:", emailframe.loc[emailframe['type'] == 0].shape[0])
print("ham in rows:", emailframe.loc[emailframe['type'] == 1].shape[0])

stopwords = codecs.open('stopwords.txt', 'r', 'UTF8').read().split('\r\n')

# cut words and process text
processed_texts = []
for text in emailframe["text"]:
    print(text)
    words = []
    seg_list = text.split(" ")
    for seg in seg_list:
        if (seg.isalpha()) & (seg not in stopwords):
            words.append(seg)
    sentence = " ".join(words)
    processed_texts.append(sentence)
emailframe["text"] = processed_texts

emailframe.to_csv("filter_full_email_label.csv")
