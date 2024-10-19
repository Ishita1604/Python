import numpy as np
import pandas as pd

print('------------------------------------------------------------------------------------------------------------')
data = np.arange(0, 20).reshape(5, 4)
print(data, '\n')

df = pd.DataFrame(data, index=['Row1','Row2','Row3','Row4','Row5'], columns=['Col1','Col2','Col3','Col4'])

print(df, '\n\n')
print(df.head(2)) # By default gives first five rows.
print(df.tail(1)) # By default gives last five rows.
print('\n', type(df), '\n')
print(df.info(), '\n') # How many rows, columns and their datatypes.

print(df.describe(), '\n') # Statistical data.



# Indexing in Pandas DataFrame:
# Using column name -
print(df['Col1'])
print(type(df['Col1'])) # Single row or column is of "Series" datatype.
print(df[['Col1', 'Col2', 'Col4']])
print(type(df[['Col1', 'Col2', 'Col4']])) # Multiple rows and columns is of "DataFrame" datatype.


# Using row index and "loc" -
print(df.loc['Row1'])
print(type(df.loc['Row1']), '\n')

print(df.loc[['Row1', 'Row5']])
print(type(df.loc[['Row1', 'Row5']]), '\n')


# Using both row and column index and "iloc" -
print(df.iloc[2:4, :2])


# Convert DataFrame to arrays -
ar = df.iloc[1:3, 1:].values
print(ar)


arr = [[1, np.nan, 2], [2, 3, 4]] # Must be a 2D list to become "DataFrame".
print(arr, '\n')
# Interesting to note, "NaN" by default takes float datatype.


df2 = pd.DataFrame(data=arr, index=['Row1', 'Row2'], columns=['Col1','Col2','Col3'])
print(df2, '\n')
print(df2.info(), '\n')

print(df2.isnull(), '\n') # Returns a DataFrame.


# The sum() method gives column-wise info.
print(df2.isnull().sum(), '\n') # Gives count of "NaN" values of each column.

print(df2.isnull().sum()==0, '\n') # Boolean result of whether column contains "NaN" or not. True indicates "NaN" is not present.

print(df2['Col3'].value_counts(), '\n')

print(df2['Col3'].unique(), '\n') # Unique values as in count of non-repititive values.

print(df2[df2['Col3']>3], '\n') # That row that has value greater than 3 in column 3.
