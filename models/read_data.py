import numpy as np
import pandas as pd
from datetime import datetime
import time

from sklearn import preprocessing


def read_csv(path):
    df = pd.read_csv(path)
    df = df.sample(frac=1)
    # print(len(df))
    # print(list(df['unhealth']))
    # print(df.head)
    features = np.column_stack((df['afinn_score'],
                                df['syllable_count'], df['difficult_words'], df['flesch_reading_ease'],
                                df['flesch_kincaid_grade'], df['coleman_liau_index'], df['automated_readability_index'],
                                df['gunning_fog'],
                                df['linsear_write_formula'],
                                df['dale_chall_readability_score'],
                                df['crawford'],
                                df['gutierrez_polini'],
                                # df['date'],
                                # df['hour'],
                                df['followers_count'],
                                df['friends_count'], df['favourites_count'],
                                df['bow_i'], df['bow_depression'],
                                # df['bow_diagnosed'],
                                df['bow_you'], df['bow_like'],

                                ))

    # print(features[0])
    return features, list(df['unhealth'])


def read_predic_csv(path):
    df = pd.read_csv(path)
    df = df.sample(frac=1)
    # print(len(df))
    # print(list(df['unhealth']))
    # print(df.head)
    features = np.column_stack((df['afinn_score'],
                                df['syllable_count'], df['difficult_words'], df['flesch_reading_ease'],
                                df['flesch_kincaid_grade'], df['coleman_liau_index'], df['automated_readability_index'],
                                df['gunning_fog'],
                                df['linsear_write_formula'],
                                df['dale_chall_readability_score'],
                                df['crawford'],
                                df['gutierrez_polini'],
                                # df['date'],
                                # df['hour'],
                                df['followers_count'],
                                df['friends_count'], df['favourites_count'],
                                df['bow_i'], df['bow_depression'],
                                # df['bow_diagnosed'],
                                df['bow_you'],
                                df['bow_like'],

                                ))

    # print(features[0])
    return features


def data():
    weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny',
               'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']  # 14
    temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot',
            'Mild']  # 14

    play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']  # 14

    # creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    wheather_encoded = le.fit_transform(weather)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(temp)
    label = le.fit_transform(play)

    print("weather:", wheather_encoded)
    print("Temp:", temp_encoded)
    print("Play:", label)
    print(len(label))

    # Combinig weather and temp into single listof tuples
    features = np.column_stack((wheather_encoded, temp_encoded))
    # print(features)
    return (features, label)
