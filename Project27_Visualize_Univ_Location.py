"""

"""

import pandas as pd
import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'
road_type2 = 'PARCEL'
address = '&address='
keys = '&key='
primary_key = ' --- '

def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] =='OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x,y
    else:
        x = 0
        y = 0
        return 0
    
x,y = request_geo('경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)')

print(f'x값: {x}')
print(f'y값: {y}')

"""
filePath = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/고등교육기관 주소록(2022).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].tolist()

df_from_excel = df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)
print(df_from_excel['주소'].values)
"""