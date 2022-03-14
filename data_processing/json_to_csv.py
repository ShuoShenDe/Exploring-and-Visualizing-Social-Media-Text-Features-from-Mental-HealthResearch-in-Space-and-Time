import pandas as pd
import csv
import json
import demoji
from unidecode import unidecode

# demoji.download_codes()  # get all emojis/ update emojis

dict_data = dict()
csv_columns = ['user', 'created_at', 'text', 'geo', 'coordinates', 'place', 'followers_count', 'friends_count', 'favorite_count']
csv_file = 'nyc_data_5.csv'


try:
    with open(csv_file, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
except IOError:
    print("ERROR 1")


def remove_non_ascii(text):
    return unidecode(unidecode(text))


with open('C:/Users/maxim/Documents/TUM/4. Master/Selected Topics - Big Geospatial Data/stream_nyc_box_weekend_20210716-105934.jsonl', 'r') as json_file:
    json_list = list(json_file)

    for json_str in json_list:
        dict_tempdata = json.loads(json_str)

        for d in dict_tempdata:
            dict_data['user'] = remove_non_ascii(demoji.replace_with_desc(dict_tempdata['user']['screen_name']))
            dict_data['created_at'] = dict_tempdata['created_at']
            dict_data['text'] = remove_non_ascii(demoji.replace_with_desc(dict_tempdata['text']))
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
            dict_data['followers_count'] = dict_tempdata['user']['followers_count']
            dict_data['friends_count'] = dict_tempdata['user']['friends_count']
            dict_data['favorite_count'] = dict_tempdata['favorite_count']

        try:
            with open(csv_file, 'a', newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writerow(dict_data)
        except IOError:
            print("ERROR 2")
