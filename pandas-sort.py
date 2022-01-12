import pandas as pd

df = pd.read_csv("C:\\Users\\vishw\\OneDrive\\Documents\\pythonlearn\\state.csv")

df1 = pd.DataFrame({'state': 'az', 'revenue': 50}, index=[0, 1])

df3 = pd.merge(df,df1,how='inner',on='state')
print(df)
print(df1)
print(df3)

# print(df)
# df.fillna(99,inplace=True)
# print(df)
# print(df.shape)
# print(df.describe())
# print(df.groupby('year')['revenue'].sum())
# print(df[df['year']==2010])


# df1= df.groupby('state')['revenue'].sum()
# print(df1)

# print('sorted values')
# print(df.sort_values('music'))
# print('sort by index')
# print(df.sort_index(axis=1, ascending=True))
# print('after hiding indexes')
# print(df.to_string(index=False))
# print('show column')
# print(df.columns)

# axis 0 for axis 1 for row
# print(df[:1])
# print(df.sort_values('age'))
# print(df.loc[0])
# print(df.loc[0,'food'])  # cut by index

# index are kind of rows and columns are columns
