import xlrd
import pandas as pd
import numpy as np

import os ,sys

df = pd.read_csv(f"C:/Users/Student/Desktop/project/19952022.csv")


df.columns

df = df.drop(['警報期間.1'],axis = 1)
df = df.drop(['Unnamed: 12'],axis = 1)

df_date = df["年份"].ffill()
df_close = df["近臺強度"].ffill()
df_min_p = df["近臺最低氣壓(hPa)"].ffill()
df_wp = df["近臺最大風速(m/s)"].ffill()
df_7level = df["近臺7級風暴風半徑(km)"].ffill()
df_10level = df["近臺10級風暴風半徑(km)"].ffill()
df_alarm = df["警報發布報數"].ffill()
df_typhon_number = df["颱風編號"].ffill()
df_time = []


for dt in df['警報期間']:
    df_times = dt.split(' ')[0]
    df_time.append(df_times)
    
df_time = pd.DataFrame(df_time,columns=["date"]) 

df_time["date"] = df_time["date"].str.replace('/','-')
    
   
df2 = pd.DataFrame()


df2 = pd.concat([df2,df_time],axis=1)
df2 = pd.concat([df2,df_close],axis=1)   
df2 = pd.concat([df2,df_alarm],axis=1)



size_mapping = {
    '強烈': 3,
    '中度': 2,
    '輕度':1
 }

df2["近臺強度"] = df2["近臺強度"].map(size_mapping)
df2["level"] = df2["近臺強度"]
df2 = df2.drop(["近臺強度"],axis=1)

df2["alarms_count"] = df2["警報發布報數"]
df2 = df2.drop(["警報發布報數"],axis=1)
    
df2.to_csv('C:/Users/Student/Desktop/typhon.csv')    

wheather_df = pd.read_csv(f"C:/Users/Student/Desktop/project/allconcat.csv")
price_df = pd.read_csv(f"C:/Users/Student/Desktop/project/9-12.xls")

all_df =wheather_df.merge(df2, how='left', on='date')

all_df["level"] = 0
all_df["alarms_count"] = 0

all_df =all_df.merge(price_df, how='left', on='date')



all_df = all_df.dropna()

all_df = all_df.reindex(columns=['date', 'month', 'year', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',
       'Sun', 'pressure', 'temperature', 'humidity', 'windspeed',
       'wind_direction', 'maximum_windspeed', 'maximum_wind_direction',
       'rainfall', 'volume', 'level', 'alarms_count', 'price', 'D+1', 'D+3','D+5',
       'D+7'])

all_df.columns
all_df.to_csv('C:/Users/Student/Desktop/project/augest.csv')    






