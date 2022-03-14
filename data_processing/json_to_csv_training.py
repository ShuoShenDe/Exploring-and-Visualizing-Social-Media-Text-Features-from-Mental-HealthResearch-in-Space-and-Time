import pandas as pd
import csv
import json
import demoji
from unidecode import unidecode
from os import walk
import os
from random import *
demoji.download_codes()  # get all emojis/ update emojis


dict_data = dict()
csv_columns = ['unhealth','user', 'created_at', 'text', 'geo', 'coordinates', 'place','json_name','followers_count','friends_count','favourites_count']
csv_file = './code/bgd_mentalhealth/bgd_mentalhealth/training_data/trainning_neg.csv'

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
except IOError:
    print("ERROR 1")

def remove_non_ascii(text):
    return unidecode(unidecode(text))


path="./labeled/negative/data/tweet/"
json_file_names = os.listdir(path)
for json_file_name in json_file_names:
    with open(path+json_file_name, 'r') as json_file:
        json_list = list(json_file)
        for json_str in json_list:
            dict_tempdata = json.loads(json_str)            
            if dict_tempdata['lang']!='en':
                continue

            dict_data['unhealth']=0
            dict_data['user'] = remove_non_ascii(demoji.replace_with_desc(dict_tempdata['user']['screen_name']))
            dict_data['created_at'] = dict_tempdata['created_at']
            dict_data['text'] = remove_non_ascii(demoji.replace_with_desc(dict_tempdata['text']))
            dict_data['json_name']=json_file_name
            dict_data['followers_count'] = dict_tempdata['user']['followers_count']
            dict_data['friends_count'] = dict_tempdata['user']['friends_count']
            dict_data['favourites_count'] = dict_tempdata['user']['favourites_count']

            try:
                dict_data['geo'] = dict_tempdata['geo']['type']
            except TypeError:
                dict_data['geo'] = 'None'
            try:
                dict_data['coordinates'] = dict_tempdata['geo']['coordinates']
            except TypeError:
                dict_data['coordinates'] = 'None'
            try:
                dict_data['place'] = remove_non_ascii(demoji.replace_with_desc(dict_tempdata['place']['name']))
            except TypeError:
                dict_data['place'] = 'None'
            

        try:
            with open(csv_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writerow(dict_data)
        except IOError:
            print("ERROR 2")
