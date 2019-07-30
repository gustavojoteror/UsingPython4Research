#GOAL" learn how to calculate and plot daily mean speed
# we want to create a plot where the y-axis is the average speed/per day and in the x-axis the time in days
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

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
birddata['timestamp'] = pd.Series(timestamps, index= birddata.index)
data = birddata[birddata.bird_name == 'Eric']
times = data.timestamp
speed2D = np.array(data.speed_2d)
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)


# gustavo
next_day = 1
avg_speed=0
count=1

time = []
speed= []
for i, d in enumerate(elapsed_days):
    if d > next_day :
        avg_speed /= count
        time.append(next_day-1)  # to start at 0
        speed.append(avg_speed)

        next_day +=1
        avg_speed=0
        count=1
    else:
        if ~np.isnan(speed2D[i]):
            avg_speed = (avg_speed + speed2D[i])
            count+=1



# course:
next_day = 1
inds= []
daily_mean_speed= []
for i, t in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day +=1
        inds = []


k=len(daily_mean_speed)
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed[0:k], label = 'course')
plt.plot(time[0:k], speed[0:k], label = 'gustavo')
plt.xlabel('Day')
plt.ylabel('Mean speed [m/s]')
plt.legend(loc='lower right')
plt.savefig('DailyMeanSpeed.pdf')

