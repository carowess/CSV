import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")
open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")
csv_file2 =csv.reader(open_file2,delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

location_title = next(csv_file) 
location_title2 = next(csv_file2) 

def index_match(title,key):
    for index in title:
        if index == key:
            return title.index(index)

##SITKA

sitka_lows = []
sitka_highs = []
sitka_dates = []

for row in csv_file:
    try: 
        the_date = datetime.strptime(str(row[index_match(header_row,"DATE")]),'%Y-%m-%d')
        high = int(row[int(index_match(header_row,"TMAX"))])
        low = int(row[int(index_match(header_row,"TMIN"))])
    except ValueError:
        print(f"Missing data for {the_date}") 
    else:
        sitka_highs.append(int(row[index_match(header_row,"TMAX")]))
        sitka_lows.append(int(row[index_match(header_row,"TMIN")]))
        sitka_dates.append(the_date)
    
##DEATH VALLEY
death_lows = []
death_highs = []
death_dates = []

for row in csv_file2:
    try: 
        the_date = datetime.strptime(str(row[index_match(header_row2,"DATE")]),'%Y-%m-%d')
        high = int(row[int(index_match(header_row2,"TMAX"))])
        low = int(row[int(index_match(header_row2,"TMIN"))])
    except ValueError:
        print(f"Missing data for {the_date}") 
    else:
        death_highs.append(int(row[index_match(header_row2,"TMAX")]))
        death_lows.append(int(row[index_match(header_row2,"TMIN")]))
        death_dates.append(the_date)
        

fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(sitka_dates,sitka_highs,c="red")
plt.plot(sitka_dates,sitka_lows,c="blue")
plt.fill_between(sitka_dates,sitka_lows,sitka_highs,facecolor="blue",alpha=0.1)
plt.title(location_title[1])

plt.subplot(2,1,2)
plt.plot(death_dates,death_highs,c="red")
plt.plot(death_dates,death_lows,c="blue")
plt.fill_between(death_dates,death_lows,death_highs,facecolor="blue",alpha=0.1)
plt.title(location_title2[1])

plt.suptitle(f"Temperature comparison between {location_title[1]} and {location_title2[1]}")

fig.autofmt_xdate()

plt.show()


