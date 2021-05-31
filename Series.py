import pandas as pd

score     = [45,55,34,60,70]
statement = [True,False,True,True,False]
students  = ['Mizan','Mamun','Mahfuz','Karim','Sohag']
list      = [True,False,'Mizan',12,14,54,60]
contacts  = {
	'Mamun'   : '01916178600',
	'Mizan'   : '01916178400',
	'Mahfuz'  : '01916178200',
	'Morshed' : '01916178200',
	'Mahmood' : '01916178200'
}

# Series
pd.Series(score)
pd.Series(statement)
pd.Series(students)
pd.Series(list)
pd.Series(contacts)
pd.Series(5, index=[0])
pd.Series(5, index=[0,1,2,3,4,5])
pd.Series([2 * num for num in range(10)])
[2 * num for num in range(10)]


# Series Attributes and Mehtods
data = pd.read_csv('Stock.csv')
data = pd.read_csv('Stock.csv', usecols=['Open'])
data = pd.read_csv('Stock.csv', usecols=['Open'], squeeze=True)
data.index
data.values
data.dtype
data.ndim
data.size
data.is_unique
data.is_monotonic_increasing
data.add_prefix('product_')
data.add_suffix('_product')
data.idxmax()
data.idxmin()
data.sum()
data.mean()
data.std()
data.var()
data.min()
data.max()
data.product()
data.count()
data.describe()

temperature = [30,20,45,30,29,30,35]
weeks       = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
pd.Series(temperature, weeks)
pd.Series(data=temperature, index = weeks)
s = pd.Series(data=temperature, index = weeks)
type(s)
s.dtypes
s.index
s.values
