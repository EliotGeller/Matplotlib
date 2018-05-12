#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from matplotlib.dates import date2num, DayLocator, DateFormatter
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
# AAPL.csv
# Date,Open,High,Low,Close,Adj Close,Volume

#datetime(year,month,day,hour,minute,seconds)

f = open("AAPL.csv","r")
#{key:value} key = header names, value = [values]

data = {}

header = f.readline()
header = header.strip("\n")
header = header.split(",")

for name in header:
    data[name] = []
    
for line in f:
    line = line.strip("\n").split(",")
    date = [int(x) for x in line[0].split("-")]
    date = datetime(date[0],date[1],date[2])
    date = date2num(date)
    data['Date'].append(date)
    data['Open'].append(float(line[1]))
    data['High'].append(float(line[2]))
    data['Low'].append(float(line[3]))
    data['Close'].append(float(line[4]))
    data['Adj Close'].append(float(line[5]))
    data['Volume'].append(int(line[6]))
    
#print(data)
#print(f.readline())     
f.close()

fig = plt.figure(figsize = (10,10))
ax = plt.subplot()

plotData = []
for i in range(len(data['Date'])):
    tempData = [data['Date'][i],
                data['Open'][i],
                data['High'][i],
                data['Low'][i],
                data['Close'][i],
                data['Adj Close'][i],
                data['Volume'][i]]
    plotData.append(tempData)
    
candlestick_ohlc(ax, plotData, colorup = "green", colordown = "blue",
                 alpha = 1.0)
ax.xaxis.set_major_locator(DayLocator(1))
ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
ax.xaxis.set_minor_locator(DayLocator(range(1,32,7)))
ax.xaxis_date()

for tick in ax.xaxis.get_ticklabels():
    tick.set_rotation(45)
plt.show()

