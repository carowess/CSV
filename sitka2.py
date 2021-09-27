import csv
import matplotlib.pyplot as plt
from datetime import datetime



open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

## enumerate gives the index location and the object itself that's in that location
## ideal for assigning indexes so that it's easier access later when you're looking for a certain object but don't know the index
for index, column_header in enumerate(header_row):
    print(index, column_header)



## testing to convert date from string
mydate = datetime.strptime('2018-07-05','%Y-%m-%d')
print(mydate)
print(type(mydate))



## making the list and adding the values
highs = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(the_date)

print(highs)
print(dates)

fig = plt.figure()

## making and showing the graph
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

## this is where the data is actually added 
plt.plot(dates,highs,c="red")

fig.autofmt_xdate()

plt.show()




