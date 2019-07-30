# PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS PANDAS
# pandas is library that provides additional data structures and data analysis functionalities for python
# It's especially useful for manipulating numerical tables and time series data.
#           panda: PANel DAta whcih refer to multi-dimensipnal structure data sets.
# the most common data structure in pandas is data frame.


import pandas as pd
table = pd.DataFrame(columns= ('name', 'age'))
table.loc[1] = 'James', 22  #loc: location  loc[1] is as the first row
table.loc[2] = 'Jess', 32  #loc: location  loc[1] is as the first row

print(table)
print(table.columns)