import csv
import matplotlib.pyplot as plt
from datetime import datetime



open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

#print(type(header_row))

## enumerate gives the index location and the object itself that's in that location
## ideal for assigning indexes so that it's easier access later when you're looking for a certain object but don't know the index
#for index, column_header in enumerate(header_row):
    #print(index, column_header)



## testing to convert date from string
mydate = datetime.strptime('2018-07-05','%Y-%m-%d')
#print(mydate)
#print(type(mydate))



## making the list and adding the values
highs = []
lows = []
dates = []

for row in csv_file:
    try: 
        high = int(row[4])
        low = int(row[5])
        the_date = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print("Missing data for {the_date}") ##new method for printing!!
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)


#print(highs)
#print(dates)
#print(lows)


fig = plt.figure()

## making and showing the graph
plt.title("Daily high and low temperatures - 2018\nDeath Valley", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

## this is where the data is actually added 
## alpha is how dark or light the color is
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

fig.autofmt_xdate()

plt.show()


# arguments for this function: # of rows, # of columns, index (which one are we trying to plot?)
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()


