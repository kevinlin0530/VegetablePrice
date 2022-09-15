


import xlrd
import pandas as pd
import numpy as np
import os





path = f'C:/Users/Student/Desktop/期末專題'

dirs = os.listdir(path)

if dirs[0]=='desktop.ini':
   dirs.remove("desktop.ini")
    
    
    
df=pd.DataFrame()
for d in dirs : 
    data = pd.read_csv(f'{path}/{d}',on_bad_lines='skip')
    data.insert(1,"country",d.split('-')[0])
    data.insert(2,"location",d.split('-')[1])
    data.insert(1,"year",d.split('-')[3])
    data.insert(0,"month",d.split('-')[4].split('.')[0])
    df = pd.concat([df,data.iloc[1:,:]])

# df.to_csv('C:/Users/Student/Desktop/allconcat.csv')



df['date'] = data['year'] +'-'+data['month']+ '-' +data['觀測時間(day)']


df = df.replace('...', np.nan) 
df = df.replace('T',float(0.05))
df = df.replace('/',np.nan)
df = df.replace('X',np.nan)
df = df.replace('&',np.nan)

df.isnull().sum()/len(df.index)
df=df.dropna(thresh=5,axis=0)

mask=df.isnull().sum()/len(df.index)<0.8
df2=df.loc[:,mask]

df2.columns
df2["pressure"] = df.loc[:,'測站氣壓(hPa)']
df2['maximum_pressure'] = df.loc[:,'測站最高氣壓(hPa)']
df2['minimum_pressure'] = df.loc[:,'測站最低氣壓(hPa)']
df2['temperature'] = df.loc[:,'氣溫(℃)']
df2["maximum_temperature"] = df.loc[:,'最高氣溫(℃)']
df2['minimum_temperature'] = df.loc[:,'最低氣溫(℃)']
df2['humidity'] = df.loc[:,'相對溼度(%)']
df2['minimum_humidity'] = df.loc[:,'最小相對溼度(%)']
df2['windspeed'] = df.loc[:,'風速(m/s)']
df2['wind_direction'] = df.loc[:,'風向(360degree)']
df2['maximum_windspeed'] = df.loc[:,'最大陣風(m/s)']
df2['maximum_wind_direction'] = df.loc[:,'最大陣風風向(360degree)']
df2['rainfall'] = df.loc[:,'降水量(mm)']

df3 = df2.iloc[:,[0,1,2,3,4,24,25,26,27,28,29,30,31,32,33,34,35,36,37]]

df4 = df2.iloc[:,[0,2,25,26,27,28,29,30,31,32,33,34,35,36,37]].astype(float)

df4["country"] = df3.iloc[:,3]                                                   
    

                                                  
for i in ['pressure','maximum_pressure','minimum_pressure','temperature','maximum_temperature','minimum_temperature','humidity','minimum_humidity','windspeed','wind_direction','maximum_windspeed','maximum_wind_direction','rainfall']:
    df4[i].fillna(value=df4.groupby('country')[i].transform('mean'),inplace=True)
    
df4.insert(0,"date",df3.iloc[:,5])

df5=df4.drop(["country"],axis=1)



group=df5.groupby(df5['date'])
group=group.agg('mean')
group.insert(0,"date",group.index)


group.iloc[:,0]=pd.to_datetime(group.iloc[:,0]).dt.weekday
weekday_transfer={
    0:'Sun',
    1:'Mon',
    2:'Tue',
    3:'Wed',
    4:'Thu',
    5:'Fri',
    6:'Sat'}
group.iloc[:,0]=group.iloc[:,0].map(weekday_transfer)


group_date = pd.get_dummies(group.iloc[:,0])



group = group.drop(['date'], axis=1)


group = pd.concat([group,group_date],axis=1)


group.columns


group = group[['month', 'year', 'Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'pressure','temperature', 'humidity', 'windspeed', 'wind_direction', 'maximum_windspeed','maximum_wind_direction', 'rainfall']]

group.to_csv('C:/Users/Student/Desktop/project/allconcat.csv')
