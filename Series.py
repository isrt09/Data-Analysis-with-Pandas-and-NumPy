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