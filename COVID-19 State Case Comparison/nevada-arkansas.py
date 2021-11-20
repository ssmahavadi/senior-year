import csv
from datetime import datetime
import matplotlib.pyplot as plt
import collections
import itertools
import numpy as np
import matplotlib.dates as mdates

# state populations....go back and get more accurate numbers
arPop = 3013825
nvPop = 3034392

# gather total number of cases per day
filename = 'states_daily_4pm_et.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    ar = []
    nv = []

    for row in itertools.islice(reader, 170, 8792):
        if str(row[1]).find("AR") != -1:
            date = datetime.strptime(row[0], "%Y%m%d")
            dates.append(date.strftime("%m/%d"))
            ar.append(int(row[2]))
        if str(row[1]).find("NV") != -1:
            nv.append(int(row[2]))
dates.reverse()
ar.reverse()
nv.reverse()
'''
arData = []
nvData = []
for i in range (len(dates)):
    arData.append(ar[i]/arPop)
    nvData.append(nv[i]/nvPop)
    
'''
# plot line graph
fig = plt.figure(dpi =128, figsize=(10,6))
plt.plot(dates, ar, c='palevioletred', label='Arkansas: 3,013,825', linewidth=2.5)
plt.plot(dates, nv, c='lightsteelblue', label='Nevada: 3,034,392', linewidth=2.5)

# format plot
plt.title("Spread of Covid in AR vs NV", fontname='arial rounded mt bold', fontsize=26, fontweight='bold')
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
