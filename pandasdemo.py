import pandas as pd
import numpy as np

#Series


s1 = pd.Series()
#print s1

data = np.array(['apple','banana','carrot','dill pickle'])
s2 = pd.Series(data)
#print s2

s3 = pd.Series(data, index=[24,25,26,27])
#print s3

dictionary = {'humpty' : 10, 'dumpty' : 12, 'eggs' : 14}
s4 = pd.Series(dictionary)
#print s4

s5 = pd.Series(dictionary,index=['humpty','eggs'])
#print s5

s6 = pd.Series(dictionary,index=['humpty','eggs','wall'])
#print s6

period= {'Math' : 7, 'Cycling' : 1, 'Graphics' : 10, 'SoftDev' : 9, 'WaterColor' : 2}
s7 = pd.Series(period)
#print s7
#print s7[0]
#print s7[:3]
#print s7[2:4]
#print s7['Math']
#print s7[['SoftDev', 'Graphics']]

data = [['Alex',10],['Bob',12],['Clarke',13]]
df1 = pd.DataFrame(data,columns=['Name','Age'], index=['Entry1', 'Entry2', 'Entry3'])
#print df1

d = {'one' : pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
      'two' : pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])}

anotherd = {'one' : pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
      'two' : pd.Series([6.0, 7.0, 8.0, 10.0], index=['a', 'b', 'c', 'd']),
      'three' : pd.Series([7.0, 3.0, 11.0, 12.0], index=['a', 'b', 'c', 'd'])}

df2 = pd.DataFrame(d)
#print d['one']
#print d['two']
#print df2
#print df2.dropna()

df2 = pd.DataFrame(anotherd)
#print df2
#print df2.mean(1)

#DataFrame from https://pandas.pydata.org/pandas-docs/stable/10min.html
dates = pd.date_range('20180302', periods=6)
df3 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print df3
#print df3.index
#print df3.columns
#print df3.describe()

#print "printing sorted by index, descending..."
#print df3.sort_index(axis=1, ascending=False)
#print "\nprinting sorted by B..."
#print df3.sort_values(by='B')
#print "\nprinting elements where C > 0..."
#print df3[df3.C > 0]

#print "\nprinting mean by column..."
#print df3.mean()
#print "\nprinting mean by row..."
#print df3.mean(1)

rangelist = df3.apply(lambda x: x.max() - x.min())
#print rangelist
