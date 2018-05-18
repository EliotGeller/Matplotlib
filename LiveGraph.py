#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from random import gauss

fig = plt.figure()
ax = plt.subplot()

xdata = []
ydata = []

line,  = ax.plot(xdata, ydata)
ax.set_xlim(0,20)
ax.set_ylim(0,20)
minx = 0
maxx = 20
miny = 5
maxy = 15

def data_gen():
    counter = 0
    while counter < 100:
        counter += 1
        yield counter
        
        
def run(data):
    xdata.append(data)
    
    rv = gauss(10,1)
    
    global maxy
    global miny
    

    if rv > maxy:
        maxy = rv
    elif rv < miny:
        miny = rv
        
    ydata.append(rv)
    
    global maxx
    global minx
    
    if data > maxx:
        maxx = data
        ax.set_xlim(xdata[-20], xdata[-1])
        ax.set_ylim(miny, maxy)
    
    line.set_data(xdata, ydata)
    return line

ani = FuncAnimation(fig, run, data_gen, interval = 200, repeat = False)
plt.show()

