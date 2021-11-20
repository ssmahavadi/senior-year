import csv
from datetime import datetime
import matplotlib.pyplot as plt
import collections


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highLows = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highLows.append(high-low)

counter = collections.Counter(highLows)
frequency = counter.values()
differences = counter.keys()

#plt.pie(freq, labels=differences, autopct='%1.1f%%')   # With percentages
plt.pie(frequency, labels=differences)    
plt.axis('equal')
plt.title("Differences in High and Low Temperatures")

plt.show()
