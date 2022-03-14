import pandas as pd

list_df = []

csv_1 = pd.read_csv('wdc_data_1.csv')
csv_2 = pd.read_csv('wdc_data_2.csv')
csv_3 = pd.read_csv('wdc_data_3.csv')
csv_4 = pd.read_csv('wdc_data_4.csv')
csv_5 = pd.read_csv('wdc_data_5.csv')

list_df.append(csv_1)
list_df.append(csv_2)
list_df.append(csv_3)
list_df.append(csv_4)
list_df.append(csv_5)

merged_df = pd.concat(list_df)

merged_df.to_csv('concat_wdc_data_0308.csv')
