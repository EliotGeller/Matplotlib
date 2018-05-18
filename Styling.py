#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib

#print(matplotlib.style.available)

matplotlib.style.use("classic")

#print(matplotlib.rcParams.keys())

matplotlib.rcParams["lines.linewidth"] = 5 
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.labelsize"] = 20
matplotlib.rcParams["axes.titlesize"] = 25

plt.xkcd()

xdata = []
ydata = []

fig = plt.figure(figsize = (8,8))

for i in range(20):
    xdata.append(i)
    ydata.append(i)
    
plt.grid()
plt.plot(xdata, ydata, label = "Plot 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X and Y axis")
plt.legend(loc = "lower right")
plt.show()

