import pandas as pd
import re

csv_file = pd.read_csv('concat_nyc_data_0308.csv')

df = pd.DataFrame(csv_file)
drop_list = []

for i in range(0, len(df)):
    text = df.iloc[i]['text']
    if re.match('Just posted a photo @', str(text)):
        # print(df.iloc[i]['text'])
        # print('-')
        drop_list.append(i)

df_wo_pics = df.drop(drop_list)

df_wo_pics.to_csv('nyc_data_0308_wo_pics.csv')
