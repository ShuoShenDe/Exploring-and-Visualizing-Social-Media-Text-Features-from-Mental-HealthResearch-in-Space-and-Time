import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import csv


input_data = []
readata = pd.read_csv("trainning_neg.csv")
input_data = readata['text'].astype(str).values.tolist()
my_stop_words = []

# without smooth IDF
print("Without Smoothing:")
# define tf-idf
tf_idf_vec = TfidfVectorizer(use_idf=False, stop_words=my_stop_words, token_pattern='(?u)\\b\\w+\\b', lowercase=True, analyzer='word', norm="l1")  # to use only  bigrams ngram_range=(2,2)

#tokenizer=lambda doc: doc
# transform
with open('Bow.csv', 'w', encoding='UTF8') as w:
    writer = csv.writer(w)
    for i in range(0, len(input_data)):
        tf_idf_data = tf_idf_vec.fit_transform([input_data[i]])
        for d in range(0, tf_idf_data.shape[0]):
            #tf_idf_data.getrow(d).toarray()[0]
            tf_idf_dataframe = pd.DataFrame(tf_idf_data.getrow(d).toarray(), columns=tf_idf_vec.get_feature_names())
            #tf_idf_dataframe.to_csv('Bow.csv', encoding='utf-8', index=False, line_terminator='\n')
            writer.writerow(tf_idf_dataframe)

# create dataframe
#tf_idf_dataframe = pd.DataFrame(tf_idf_data.toarray(), columns=tf_idf_vec.get_feature_names())
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(tf_idf_dataframe)

print("\n")

# Source : https://www.mygreatlearning.com/blog/bag-of-words/
'''
with open('Bow.csv', 'w', encoding='UTF8') as w:
    writer = csv.writer(w)
    writer.writerows(tf_idf_dataframe)
'''
#tf_idf_dataframe.to_csv('Bow.csv', encoding='utf-8', index=False, line_terminator='\n')
