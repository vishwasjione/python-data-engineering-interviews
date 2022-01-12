import pandas as pd
import numpy as np

s = pd.Series([2,3,4,np.nan,8,9,10])
# print(s)

d = pd.date_range('20200301',periods=10)
# print(d)

df= pd.DataFrame(np.random.randn(10,4), index=d,columns=['A','B','C','D'])
# print(df)

df = pd.DataFrame({'A':[1,2,3,4],'B':pd.Timestamp('20200301'),'C':pd.Series(1,index=list(range(4)))})

df1=pd.read_csv("C:\\Users\\vishw\\OneDrive\\Documents\\pythonlearn\\abc.csv")
df2=pd.read_csv("C:\\Users\\vishw\\OneDrive\\Documents\\pythonlearn\\cde.csv")

print(df2)
print(df2.sort_index(axis=1,ascending=False))

# print columns
print("print column names")
print(df2.columns)
# data statistics
print("describe dataframe")
df2.describe()
print(df2.describe())

print("print a single column")
onlycolumn=df2['name']
print(onlycolumn)

print('filter by a column')
df3 = df2.loc[df2['name']=='diva']
print(df3)
print("create a dataframe from a column")
df4=df2['food']
print(df4)

# boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
#          'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
#          'Price': [10,15,5,5,10,15,15,5]
#         }
#
# df = pd.DataFrame(boxes, columns= ['Color','Shape','Price'])
#
# select_color = df.loc[df['Color'] == 'Green']
# print (select_color)

# print(df2)
# print(df2.shape)
# print(df2.head(2))
# print(df2.tail(2))
# print(df2.index)
# print(df2)
# print(df1.columns)
# print(df1.dtypes)
# print(df1)
# print(pd.__version__)

# print(v)