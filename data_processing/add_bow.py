import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

csv_s = pd.read_csv('wdc_data_0308_wo_pics.csv')
df = pd.DataFrame(csv_s)

input_data = []
input_data = csv_s['text'].astype(str).values.tolist()
my_stop_words = []

tf_idf_vec = TfidfVectorizer(use_idf=False, stop_words=my_stop_words, token_pattern='(?u)\\b\\w+\\b', lowercase=True, analyzer='word', norm="l1")  # to use only  bigrams ngram_range=(2,2)
df_zero = pd.DataFrame(0, index=np.arange(len(input_data)), columns=['i', 'depression', 'diagnosed', 'you', 'like'])
tf_idf_dataframe = pd.DataFrame(columns=['i', 'depression', 'diagnosed', 'you', 'like'])

list_i = []
list_you = []
list_like = []
list_depression = []
list_diagnosed = []

for i in range(0, len(input_data)):
    try:
        tf_idf_data = tf_idf_vec.fit_transform([input_data[i]])
        data = pd.DataFrame.sparse.from_spmatrix(tf_idf_data, columns=tf_idf_vec.get_feature_names())
    except ValueError:
        print('ValueError: empty vocabulary')


    try:
        list_i.append(data['i'][0])
    except:
        list_i.append(0)

    try:
        list_you.append(data['you'][0])
    except:
        list_you.append(0)

    try:
        list_like.append(data['like'][0])
    except:
        list_like.append(0)

    try:
        list_depression.append(data['depression'][0])
    except:
        list_depression.append(0)

    try:
        list_diagnosed.append(data['diagnosed'][0])
    except:
        list_diagnosed.append(0)

array_i = np.array(list_i)
array_you = np.array(list_you)
array_like = np.array(list_like)
array_depression = np.array(list_depression)
array_diagnosed = np.array(list_diagnosed)

df['bow_i'] = array_i
df['bow_depression'] = array_depression
df['bow_diagnosed'] = array_diagnosed
df['bow_you'] = array_you
df['bow_like'] = array_like

df.to_csv('wdc_0308.csv')
