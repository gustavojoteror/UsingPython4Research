import numpy as no
import pandas as pd

whisky= pd.read_csv('whiskies.txt')
whisky['Region']= pd.read_csv('regions.txt')

#printing the first and last elements of the data frame
print(whisky.head())
print(whisky.tail())

# let's index the data frame by location in the array
print(whisky.iloc[5:10, 0:5])#[rows , columns]
print(whisky.columns)       # to see all the column types
# what is printed from columns
# Index(['RowID', 'Distillery', 'Body', 'Sweetness', 'Smoky', 'Medicinal',
#       'Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty', 'Malty', 'Fruity',
#       'Floral', 'Postcode', ' Latitude', ' Longitude', 'Region'],
#       dtype='object')
# the flavors goes from body to Floral (so column 2 to 13
flavors = whisky.iloc[:, 2:14]  # first index is inclusive second index is exclusive that why we put 14
print(flavors.head())
print(flavors.columns)