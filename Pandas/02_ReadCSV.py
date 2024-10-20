import numpy as np
import pandas as pd # Python library to analyze data, short form for "Panel Data".

from io import StringIO

# Pandas can read CSV, JSON, Excel file, HTML file, etc.

print('------------------------------------------------------------------------------------------------------------')
df1 = pd.read_csv('customers.csv')
print(df1.head(), '\n')
print(df1.to_string(), '\n')


# But it can read only file-fomatted data i.e. data saved in a file.
# For string-formatted data, it is first converted to in-memory file-format, and then read_csv() done.
# StringIO is used for this.

data = ('col1,col2,col3,col4\n'
        'x,y,1,\n'
        'a,b,2,2\n'
        's,t,3,0.3\n')
# When strings placed next to each other without commas, Python concatenates them to single string.
# Brackets are just to span to multiple lines, so isn't  a tuple.

print(data, '\n')
print(type(data), '\n') # String format.
print(StringIO(data), '\n') # In-memory-file format.



print('---- DataFrame 1 ----')
df = pd.read_csv(StringIO(data)) # Read the data into a DataFrame.
print(df, '\n')
print(type(df), '\n')
print(df.info(), '\n')


print('---- DataFrame 2 ----')
df2 = pd.read_csv(StringIO(data), usecols=['col1', 'col4'])
print(df2, '\n')
print(df2.info(), '\n')


print('---- DataFrame 3 ----')
df3 = pd.read_csv(StringIO(data), dtype='object') # Specify the datatype of entire dataset. 'Object' means string.
print(df3.dtypes, '\n')

df4 = pd.read_csv(StringIO(data), dtype={'col1': object,
                                         'col3': float,
                                         'col4': object}) # Specify different datatypes to different columns.                            

# Column 2 will keep its default datatype, which is 'object'.
print(df4.dtypes, '\n')


df.to_csv('test.csv', index=False) # Convert DataFrame to new CSV file, and avoid the default serial numbers.

print('\n', df.isnull().sum(), '\n')
print(df['col1'], '\n')
print(df['col1'][0], '\n')


# Specify a certain column as index, instead of default serial numbers.
df5 = pd.read_csv(StringIO(data), index_col=2)
print(df5)

# The "usecols" extracts only those columns. And layout also changes. That's why "index_col" passed as 1.
df6 = pd.read_csv(StringIO(data), usecols=['col1', 'col3', 'col4'], index_col=1)
print(df6, '\n')



print('---- Tab Separated String Data ----')
tab_data = ('1    x    y\n'
            '2    a    b\n'
            '3    u    v\n')
print(tab_data, '\n')

print('---- Tab Seperated to DataFrame ----')
tab_df = pd.read_csv(StringIO(tab_data), sep='    ')
# tab_df = pd.read_csv(StringIO(tab_data), sep='\t')
print(tab_df, '\n')

