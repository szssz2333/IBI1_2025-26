import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/shizh/Desktop/IBI1/Week10/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

df=dalys_data.iloc[0:10,[2,3]]
print(df)
#1998 reported the maxmium DALYS

df1=dalys_data.loc[dalys_data['Entity']=='Zimbabwe',]
print(df1)
#start at 1990 and finish at 2019

df_2019=dalys_data.loc[dalys_data['Year']==2019,]
df_2019=df_2019.sort_values(by='DALYs')
print(df_2019)
print(df_2019.head(1),df_2019.tail(1))
#Highest: Lesotho, Lowest: Singapore

df_singapore=dalys_data.loc[dalys_data['Entity']=='Singapore']
plt.figure(figsize=(10, 5))
plt.plot(df_singapore.Year,df_singapore.DALYs,'bo-')
plt.title("Singapore DALYs Over Time (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=-90)
plt.tight_layout()
plt.show()

#Q:What was the distribution of DALYs across all countries in 2019?
plt.figure(figsize=(10, 5))
plt.scatter([1]*len(df_2019),df_2019["DALYs"],s=10)
plt.boxplot(df_2019["DALYs"],sym='')
plt.gca().xaxis.set_visible(False)
plt.title("2019 Global DALYs Distribution (Scatter & Box Plot)")
plt.ylabel("DALYs per capita")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()