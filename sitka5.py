import csv
import matplotlib.pyplot as plt
from datetime import datetime

#def get_weather_data(open_file,highs,lows,dates,date_index,high_index,low_index,name_index):
open_file = open("death_valley_2018_simple.csv", "r")
open_file = open('sitka_weather_2018_simple.csv',"r")

with open(open_file) as f:
    csv_file = csv.reader(open_file,delimiter=",")
    header_row = next(csv_file)

    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

def get_weather_data(highs,lows,dates,date_index,high_index,low_index,name_index):
    for row in csv_file:
        the_date = datetime.strptime(row[date_index],'%Y-%m-%d')
        try: 
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print("Missing data for {the_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(the_date)

    return date_index, high_index,low_index,name_index


#open_file = open("death_valley_2018_simple.csv", "r")

dates = []
highs = []
lows = []

get_weather_data(highs,lows,dates,date_index,high_index,low_index,name_index)

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)



#open_file = open('sitka_weather_2018_simple.csv',"r")

dates = []
highs = []
lows = []

get_weather_data(open_file,highs,lows,dates,date_index,high_index,low_index,name_index)

ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

## making and showing the graph
plt.title("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

fig.autofmt_xdate()

plt.show()

'''
# arguments for this function: # of rows, # of columns, index (which one are we trying to plot?)
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()

'''