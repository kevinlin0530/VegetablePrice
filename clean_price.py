import xlrd
import pandas as pd
import numpy as np

import os ,sys

df = pd.read_excel(f"C:/Users/Student/Desktop/project/8-9.xls")

df=df.iloc[3:,:9]


  
 
dates = df.iloc[1:,0]


for date in range(len(dates.iloc[:-1])):
    dates.iloc[date]=dates.iloc[date].replace(dates.iloc[date][0:3], 
                                              str(int(dates.iloc[date][0:3]) + 1911))



df.iloc[:,0]=df.iloc[:,0].str.replace('/','-')

df['price']  = df.iloc[1:,6]




df1 = df.iloc[1:-1,[0,8,9]]

df1 = df1.rename(columns={"Unnamed: 8": "volume"})



df1["D+1"] = df1.iloc[:,2].shift(-1)

df1["D+3"] = df1.iloc[:,2].shift(-3)

df1["D+5"] = df1.iloc[:,2].shift(-5)

df1["D+7"] = df1.iloc[:,2].shift(-7)



df1.rename(columns= {'蔬菜 產品日交易行情':'date'},inplace=True)




df1.columns
df1.to_csv(f"C:/Users/Student/Desktop/project/9-12.xls")
