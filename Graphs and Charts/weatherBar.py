import csv
from matplotlib import pyplot as plt
from datetime import datetime
from collections import Counter

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs=[]
    dates=[]
    for row in reader:
        highs.append(int(row[1]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
        
rAnge = int(input("Range of Values?: "))
datesRange = []
highRange = []

i = 0
while (i < rAnge):
    datesRange.append(dates[i])
    highRange.append(highs[i])
    i += 1

plt.bar(range(len(datesRange)), highRange)

plt.title("Max Temperature in Fahrenheit")

#add flar
plt.xticks(range(len(datesRange)), datesRange)

plt.show()

