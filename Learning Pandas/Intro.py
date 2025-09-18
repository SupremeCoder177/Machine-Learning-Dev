
import pandas as pd
import numpy as np

"""
What is pandas?

Basically in data analysis methodology model, pandas is used in the Prepare
phase, it is used to read and process data basically.

It makes data ready for analysis or modelling and it uses numpy under da hood. 

It is similar to using SQL but sometimes it can more powerful than SQL, so it is really easy to use.

But there are limitations to using pandas, following are the cases when one should not use pandas
(i) non-tabular
(ii) images 
(iii) very large amount of data (>3GB)

for such cases use only things like Spark or SQL
"""

"""
What are dataframes?

In simple words tables, or 2D matrices.

What are series?

A single column of a table, or a column vector.

So dataframes is made up of multiple series.
"""


# Making tables with matrices

# making a 2D matrix
a = np.array([[1, 2], [3, 4]])

# converting the matrix into a table
table_a = pd.DataFrame(a)

# so this will print the matrix 'a' in form of a table
print(table_a)
print()

# Making table with dictionaries

# making a list of dictionaries
data = [{"math" : 1, "science" : 2}, {"math" : 2, "science" : 5}]

# converting it into a table
table_data = pd.DataFrame(data)

print(table_data)
print()

"""
Basically think of each dictionary in the list as a row, with the dictionary keys as the column heading
"""

# another way of printing a table
# gives extra info about the table, like memory usage, data type etc
print(table_data.info())
print()

# getting a single row
print(table_data.head(1))