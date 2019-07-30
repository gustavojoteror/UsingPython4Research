#GOAL" learn how to deal with timestamped data using dateitme. Learn how to mearure elapsed time
# perform arithmetic operation with date and timestamps (calculating a time interbal between two observations)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

textfile = "bird_tracking.csv"
birddata = pd.read_csv(textfile)
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

print(birddata.date_time.head())
#      DATE STAMP TIME STAMP
#       Date       Time
# 0    2013-08-15 00:18:08+00
# 1    2013-08-15 00:48:07+00
# 2    2013-08-15 01:17:58+00
# 3    2013-08-15 01:47:51+00
# 4    2013-08-15 02:17:42+00
# note: they are all strings

# Familiarizing with datetime object
print(datetime.datetime.today())
time1 = datetime.datetime.today()


date_str = birddata.date_time[0]
print(type(date_str))
print(date_str)
print(date_str[:-3])            #slicing the string (take off the last three caracters '+00' the UTC value
#conver the string inot a datetime object
t_object = datetime.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')   # we are telling what is what in the string
                                                      #Year    #Hour
                                                         #month   #Minute
                                                             #day    #second
print(type(t_object))
print(t_object)

########################################
# let read the whole data

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))

time2 = datetime.datetime.today()
dt = time2-time1
print(dt)
print(timestamps[0:3])

# let's include this new object into the panda DataFrame (we just change it from string to datetime object
birddata['timestamp'] = pd.Series(timestamps, index= birddata.index)  # we added index so the data matches the one from the original Dataframe
print(birddata.head())
print(birddata.timestamp[4]-birddata.timestamp[3])  # time difference between the two measurements

#let's calculate all the time differences
times = birddata.timestamp[birddata.bird_name == 'Eric']
elapsed_time = [time - times[0] for time in times]          # list comprehention
# elpased_time = [0 dt1 dt1+dt2 dt1+dt2+dt3 ... ]

print(elapsed_time[0])
print(elapsed_time[1000])
print(elapsed_time[10000]/ datetime.timedelta(seconds=1))        # have the measurement in minutes
print(elapsed_time[10000]/ datetime.timedelta(minutes=1))        # have the measurement in minutes
print(elapsed_time[10000]/ datetime.timedelta(hours=24))        # have the measurement in day/24 hours
print(elapsed_time[10000]/ datetime.timedelta(days=1))        # have the measurement in days
print(elapsed_time[10000]/ datetime.timedelta(days=2))        # have the measurement in 2 days
print(elapsed_time[10000]/ datetime.timedelta(weeks=1))        # have the measurement in weeks
print(elapsed_time[10000]/ datetime.timedelta(days=365))        # have the measurement in 1 year/365 days

# let's plot the data
plt.plot(np.array(elapsed_time)/ datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel('Elapsed time [days]')
plt.savefig('timeplot.pdf')  # if it is a straight line then the elapse time is constant. However there are some jumps
