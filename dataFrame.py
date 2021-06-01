# DataFrame

import pandas as pd
import numpy as np

s = pd.Series([2,4,6])
s.index
s.values

s = pd.Series([2,4,6])
s = pd.Series([2,4,6], index=['item001','item002','item003'])
s = pd.Series([2,4,6], index=['item001','item002','item003'], columns=['A','B','C'])

names = ['age', 'workclass','fnlwgt','education','edu-num','marital-status','occupation','relationship','race','sex','cap-gain','cap-loss','hours/week','country','salary']

pd.read_csv('adult.data.csv', header=None)
df = pd.read_csv('adult.data.csv', header=None, names=names)
df.head()
df.tail()
df.index
df.values
df.shape
df.size
df.columns
df.dtypes
df.info()
df.describe()
type(df)

# Add new Column
df['Religion']     ='Muslim'
df.Religion
df['Age in Month'] = df['age'] * 12
df['age']

# multiple columns selections
df[['age','education','sex','hours/week','salary']]
select = ['age','education','salary']
report = df[select]


# Dealing with Missing Value
x  = [[np.nan,'A','B'],[np.nan,'A','B'],[3,4,np.nan]]
df = pd.DataFrame(x, columns=['A','B','C'])
df.dropna(axis=0, how='any') # row wise
df.dropna(axis=0, how='all') # row wise
df.dropna(axis=1, how='any') # column wise
df.dropna(axis=1, how='any') # column wise


# Dealing with remove Columns
y  = [[np.nan,'A','B'],[np.nan,'A','B'],[3,4,np.nan]]
df = pd.DataFrame(y, columns=['A','B','C'])
df.drop(axis=0, labels=[0])
df.drop(axis=0, labels=[0,1])
df.drop(axis=1, columns=['A'])
df.drop(axis=1, columns=['A','B'])

