import pandas as pd
import numpy as np

csv_s = pd.read_csv('nyc_03082021_final_result_.csv')
df = pd.DataFrame(csv_s)

'''
lat = []
lon = []

for i in df['coordinates']:
    if i == 'None':
        lat.append('None')
        lon.append('None')
        # NEW YORK
        # lat.append(40.707930)
        # lon.append(-74.007443)
        # WASHINGTON
        # lat.append(38.907206)
        # lon.append(-77.036696)
    else:
        temp = i.strip('][').split(',')
        lat.append(float(temp[0]))
        lon.append(float(temp[1]))

df['lat'] = lat
df['lon'] = lon


df = df.drop(columns='Unnamed: 0')
df = df.drop(columns='Unnamed: 0.1')
df = df.drop(columns='Unnamed: 0.1.1')

'''
temp_lat = df['lat']
temp_lon = df['lon']

lat = []
lon = []

for i in range(0, len(temp_lat)):
    if temp_lat[i] != 'None':
        lat.append(float(temp_lat[i]))
    else:
        lat.append(float(0))

    if temp_lon[i] != 'None':
        lon.append(float(temp_lon[i]))
    else:
        lon.append(float(0))
df['lat'] = lat
df['lon'] = lon


df.to_csv('nyc_03082021_final_result_.csv')
