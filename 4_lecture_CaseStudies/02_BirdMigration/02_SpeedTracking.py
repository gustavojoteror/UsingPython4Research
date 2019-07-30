import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

textfile = "bird_tracking.csv"
birddata = pd.read_csv(textfile)
print(birddata.info())
# What is printed
# Int64Index: 61920 entries, 0 to 61919
# Data columns (total 8 columns):
# altitude              61920 non-null int64
# date_time             61920 non-null object
# device_info_serial    61920 non-null int64
# direction             61477 non-null float64
# latitude              61920 non-null float64
# longitude             61920 non-null float64
# speed_2d              61477 non-null float64
# bird_name             61920 non-null object
# dtypes: float64(4), int64(2), object(2)
# memory usage: 4.3+ MB
# None



################################################
# let's extracte the speeda from the bird Eric and plot it
ix= birddata.bird_name == 'Eric'        # bird_name is a columnn of the data. this line return the index of Eric
speed = birddata.speed_2d[ix]
#plt.hist(speed) # gives an error
print(speed.head())
print(np.isnan(speed))      # return booleans. some are true which means that are are not a number
print(np.isnan(speed).any())      # any of them is not a number?
print(np.sum(np.isnan(speed)))      # returns how many are false (rememebr true=1 and false=0)
ind=np.isnan(speed)             # returns a boolean array
print(~ind)                     # ~ind is the complement of ind: so all the trues become false and all the false into true
plt.figure(figsize=(8,4))
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed=True)
plt.xlabel('2D speeds [m/s]')
plt.ylabel('Frequency')
plt.show()

################################################
# let's do the same but using plotting functions from pandas (they already solve the problem of the NAN)
birddata.speed_2d.plot(kind='hist', range=[0,30])
plt.xlabel('2D speeds [m/s]')
plt.ylabel('Frequency')
plt.show()
