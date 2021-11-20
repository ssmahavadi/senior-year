import csv
from datetime import datetime
import matplotlib.pyplot as plt
import collections
import itertools
import numpy as np
import matplotlib.dates as mdates

# state populations....go back and get more accurate numbers
ilPop = 12741080
paPop = 12807060

# gather total number of cases per day
filename = 'states_daily_4pm_et.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    pa = []
    il = []

    for row in itertools.islice(reader, 170, 8792):
        if str(row[1]).find("IL") != -1:
            date = datetime.strptime(row[0], "%Y%m%d")
            dates.append(date.strftime("%m/%d"))
            if not(row[2]):
                il.append(0)
            else:
                il.append(int(row[2]))
        if str(row[1]).find("PA") != -1:
            if not (row[2]):
                pa.append(0)
            else:
                pa.append(int(row[2]))
dates.reverse()
pa.reverse()
il.reverse()
'''
print(dates)
ilData = []
paData = []
for i in range (len(dates)):
    ilData.append(il[i]/ilPop)
    paData.append(pa[i]/paPop)
    '''

# plot line graph
fig = plt.figure(dpi =128, figsize=(10,6))
plt.plot(dates, il, c='teal', label='Illinois: 12,741,080', linewidth=2.5)
plt.plot(dates, pa, c='mediumblue', label='Pennsylvania: 12,807,060', linewidth=2.5)

# format plot
plt.title("Spread of Covid in IL vs PA",fontname='Arial Rounded MT Bold', fontsize=26, fontweight='bold')
plt.xlabel(' ', fontsize=16)
plt.ylabel("Positive Cases", fontsize=14)
#plt.tick_params(axis='x', which='minor', labelsize=18)
#plt.setp(plt.gca().xaxis.get_majorticklabels(),'rotation', 90)
plt.legend(loc=0, prop={'size': 12})
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_minor_locator(mdates.DayLocator())
#plt.xaxis.set_major_locator(mdates.DayLocator(interval=5))

# show plot
plt.show()

