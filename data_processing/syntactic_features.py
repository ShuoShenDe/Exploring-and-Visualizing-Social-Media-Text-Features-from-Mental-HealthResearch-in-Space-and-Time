import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from afinn import Afinn
import re
import textstat
from datetime import datetime
import time
from sklearn.model_selection import train_test_split
# nltk.download()
from random import *


def syntactic_features(text):
    afinn = Afinn()
    tags = []
    readableRow = []
    # positive or negative
    readableRow.append(afinn.score(text))
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    for index, tag in enumerate(pos_tags):
        match = re.search('\w.*', tag[1])
        if match:
            # if tag[0] == "n't" or tag[0] == "not":
            #     pos_tags[index] = (pos_tags[index][0], "NEG")
            if "VB" in tag[1]:
                tags.append(tag[1])
    tags = list(dict.fromkeys(tags))
    readableRow.append(",".join(tags))
    # text readability
    readableRow.append(textstat.syllable_count(text))  # Syllable Count
    readableRow.append(textstat.difficult_words(text))

    readableRow.append(textstat.flesch_reading_ease(text))  # How difficult a reading passage is to understand
    # print(textstat.smog_index(test_data))
    readableRow.append(textstat.flesch_kincaid_grade(text))
    readableRow.append(textstat.coleman_liau_index(text))  # grade level of the text using the Coleman-Liau Formula
    readableRow.append(textstat.automated_readability_index(
        text))  # a number that approximates the grade level needed to comprehend the text
    readableRow.append(textstat.gunning_fog(
        text))  # The index estimates the years of formal education a person needs to understand the text on the first reading
    readableRow.append(textstat.linsear_write_formula(text))  # the grade level using the Linsear Write Formula
    readableRow.append(
        textstat.dale_chall_readability_score(text))  # returns the grade level using the New Dale-Chall Formula
    readableRow.append(
        textstat.text_standard(text))  # returns the estimated school grade level required to understand the text

    readableRow.append(textstat.crawford(text))  # an estimate of the years of schooling required to understand the text
    readableRow.append(textstat.gutierrez_polini(text))  # Scores for more complex text are not reliable
    # print(textstat.fernandez_huerta(test_data))
    # print(textstat.szigriszt_pazos(test_data))
    # print(readableRow)
    readableRow.append(text)
    return readableRow


features_rows = []


def extract_syntactic_features_csv(path):
    with open(path, 'r') as file:
        reader = list(csv.reader(file))
        length = len(reader)
        print(length)
        i = 0

        # split, shuffle?
        for row in reader[1:]:
            if row != [] and textstat.lexicon_count(row[4]) != 0:
                readable_features = syntactic_features(row[4])  # text features

                # readable_features.insert(0,row[0])
                # readable_features.append(datetime.strptime(row[3], "%a %b %d %H:%M:%S +0000 %Y").strftime('%Y%m%d'))  #date
                # readable_features.append(datetime.strptime(row[3], "%a %b %d %H:%M:%S +0000 %Y").hour) #hour
                readable_features.append(row[2])  # user

                readable_features.append(row[5])  # geo

                readable_features.append(row[6])  # coordinates
                readable_features.append(row[7])  # place
                readable_features.append(row[8])  # followers_count
                readable_features.append(row[9])  # friends_count
                readable_features.append(row[10])  # favorite_count
                readable_features.append(row[11])  # bow_i
                readable_features.append(row[12])  # bow_depression
                readable_features.append(row[13])  # bow_diagnosed
                readable_features.append(row[14])  # bow_you
                readable_features.append(row[15])  # bow_like

                readable_features.append(row[16])  # lat
                readable_features.append(row[17])  # lon

                # readable_features.append(randint(0, 1))
                # readable_features.append(randint(0, 1))
                # readable_features.append(randint(0, 1))
                # readable_features.append(randint(0, 1))
                # readable_features.append(randint(0, 1))

                features_rows.append(readable_features)
                i += 1
                print(i)


# extract_syntactic_features_csv('./data_processing/training_neg_final.csv')
# extract_syntactic_features_csv('./data_processing/training_pos_final.csv')
# extract_syntactic_features_csv('./code/bgd_mentalhealth/bgd_mentalhealth/training_data/trainning_neg.csv')
extract_syntactic_features_csv('../data_processing/nyc_03082021_final.csv')

# with open('./code/bgd_mentalhealth/bgd_mentalhealth/training_data/trainning_neg.csv', 'r') as file:
#     reader = list(csv.reader(file))
#     for row in reader[1:9000]:
#         if row!=[]:
#             readable_features=syntactic_features(row[3])
#             readable_features.insert(0,row[0])
#             # print(datetime.strptime(row[2],"%a %b %d %H:%M:%S +0000 %Y").strftime('%Y%m%d'))
#             # print(datetime.strptime(row[2],"%a %b %d %H:%M:%S +0000 %Y").hour)
#             readable_features.append(datetime.strptime(row[2],"%a %b %d %H:%M:%S +0000 %Y").strftime('%Y%m%d'))
#             readable_features.append(datetime.strptime(row[2],"%a %b %d %H:%M:%S +0000 %Y").hour)

#             readable_features.append(row[8])
#             readable_features.append(row[9])
#             readable_features.append(row[10])
#             features_rows.append(readable_features)

with open('../predict/nyc_03082021_final.csv', 'w', encoding='UTF8', newline='') as w:
    writer = csv.writer(w)
    # write the header
    header = [
        # "unhealth",
        "afinn_score", "verb_tenses", "syllable_count", "difficult_words", "flesch_reading_ease",
        "flesch_kincaid_grade",
        "coleman_liau_index", "automated_readability_index",
        "gunning_fog", "linsear_write_formula", "dale_chall_readability_score", "text_standard", "crawford",
        "gutierrez_polini", "text",
        # "date","hour",
        'user',
        'geo', 'coordinates', 'place',
        "followers_count", "friends_count", "favourites_count",
        "bow_i", "bow_depression", "bow_diagnosed", "bow_you", "bow_like",
        #"unhealth"
         "lat",	"lon"

        #   'AB','SVM','LR','RF','NB'
    ]
    writer.writerow(header)
    # print(readables)
    writer.writerows(features_rows)
