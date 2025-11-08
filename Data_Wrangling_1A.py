import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv("/Users/omdevkar/Downloads/Dataset/1_employees.csv")
df
df.head()
df.head(10)
df.tail()
df.isnull()
df.isnull().sum()
df.notnull().sum()
df.notnull()
df.shape
df.describe()
df.size
df.info()
df["Bonus %"]=df["Bonus %"].astype(int)
df["Start Date"]=df["Start Date"].astype('datetime64[ns]')
df["Last Login Time"]=df["Last Login Time"].astype('datetime64[ns]')
df["Senior Management"]=df["Senior Management"].astype('bool')
df.info()
df
from sklearn.preprocessing import StandardScaler
numeric_cols = ['Salary', 'Bonus %']
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
df
df.describe()
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(6, 4))
sns.boxplot(y=df['Salary'])
plt.title('Box Plot of Salary')
plt.ylabel('Z-score')
plt.grid(True)
plt.show()
df["Gender"]=df["Gender"].replace({"Female":0,"Male":1})
df.head()
df=df.dropna()
df.info()
df["Gender"]=df["Gender"].astype('int')
df.info()
df