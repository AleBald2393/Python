pandas Basics
The first thing we'll do is install openpyxl (formerly xlrd), a module that pandas requires to read Excel files.

!mamba install openpyxl==3.0.9 -y
Next, we'll do is import two key data analysis modules: pandas and numpy.

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
Let's download and import our primary Canadian Immigration dataset using pandas's read_excel() method.

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
​
print('Data read into a pandas dataframe!')
Let's view the top 5 rows of the dataset using the head() function.

df_can.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 
We can also view the bottom 5 rows of the dataset using the tail() function.

df_can.tail()
When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. We can do this by using the info() method.

This method can be used to get a short summary of the dataframe.

df_can.info(verbose=False)
To get the list of column headers we can call upon the data frame's columns instance variable.

df_can.columns
Similarly, to get the list of indices we use the .index instance variables.

df_can.index
Note: The default type of intance variables index and columns are NOT list.

print(type(df_can.columns))
print(type(df_can.index))
To get the index and columns as lists, we can use the tolist() method.

df_can.columns.tolist()
df_can.index.tolist()
print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))
To view the dimensions of the dataframe, we use the shape instance variable of it.

# size of dataframe (rows, columns)
df_can.shape
Note: The main types stored in pandas objects are float, int, bool, datetime64[ns], datetime64[ns, tz], timedelta[ns], category, and object (string). In addition, these dtypes have item sizes, e.g. int64 and int32.

Let's clean the data set to remove a few unnecessary columns. We can use pandas drop() method as follows:

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)
Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns
We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:

df_can['Total'] = df_can.sum(axis=1)
df_can['Total']
We can check to see how many null objects we have in the dataset as follows:

df_can.isnull().sum()
Finally, let's view a quick summary of each column in our dataframe using the describe() method.

df_can.describe()

pandas Intermediate: Indexing and Selection (slicing)
Select Column
There are two ways to filter on a column name:

Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.

    df.column_name               # returns series
Method 2: More robust, and can filter on multiple columns.

    df['column']                  # returns series
    df[['column 1', 'column 2']]  # returns dataframe
Example: Let's try filtering on the list of countries ('Country').

df_can.Country  # returns a series
Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.

df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.
Select Row
There are main 2 ways to select rows:

    df.loc[label]    # filters by the labels of the index/column
    df.iloc[index]   # filters by the positions of the index/column
Before we proceed, notice that the default index of the dataset is a numeric range from 0 to 194. This makes it very difficult to do a query by a specific country. For example to search for data on Japan, we need to know the corresponding index value.

This can be fixed very easily by setting the 'Country' column as the index using set_index() method.

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.head(3)
# optional: to remove the name of the index
df_can.index.name = None
Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios: 1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985

# 1. the full row data (all columns)
df_can.loc['Japan']
# alternate methods
df_can.iloc[87]
df_can[df_can.index == 'Japan']
# 2. for year 2013
df_can.loc['Japan', 2013]
# alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]
# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]
# Alternative Method
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]
# Alternative Method
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]

Exercise: Let's view the number of immigrants from Haiti for the following scenarios:
1. The full row data (all columns)
2. For year 2000
3. For years 1990 to 1995

df_can.loc['Haiti']
df_can.loc['Haiti', 2000]

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

Exercise: Create a list named 'year' using map function for years ranging from 1990 to 2013.
Then extract the data series from the dataframe df_can for Haiti using year list.

year = list(map(str, range(1990, 2014)))
haiti = df_can.loc['Haiti', year] # passing in years 1990 - 2013

Filtering based on a criteria 
To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.

For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]
# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia
​
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
​
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

Exercise: Fetch the data where AreaName is 'Africa' and RegName is 'Southern Africa'.
Display the dataframe and find out how many instances are there?

 df_can[(df_can['Continent']=='Africa') & (df_can['Region']=='Southern Africa')]


 Sorting Values of a Dataframe or Series
You can use the sort_values() function is used to sort a DataFrame or a Series based on one or more columns.
You to specify the column(s) by which you want to sort and the order (ascending or descending). Below is the syntax to use it:-

df.sort_values(col_name, axis=0, ascending=True, inplace=False, ignore_index=False)

col_nam - the column(s) to sort by.
axis - axis along which to sort. 0 for sorting by rows (default) and 1 for sorting by columns.
ascending - to sort in ascending order (True, default) or descending order (False).
inplace - to perform the sorting operation in-place (True) or return a sorted copy (False, default).
ignore_index - to reset the index after sorting (True) or keep the original index values (False, default).

Let's sort out dataframe df_can on 'Total' column, in descending order to find out the top 5 countries that contributed the most to immigration to Canada.

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5

Exercise: Find out top 3 countries that contributes the most to immigration to Canda in the year 2010.
Display the country names with the immigrant count in this year

df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010
df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010

