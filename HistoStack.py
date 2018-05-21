#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from random import randint

fig = plt.figure(figsize = (8, 8))
ax = plt.subplot(111, projection = '3d')

color = ["red", "blue", "green", "orange", "purple"]

for z in range(5):
    x = []
    y = []
    for second in range(10):
        x.append(second)
        y.append(randint(1, 10))

    ax.bar(x, y, zs = z/2, zdir = 'y', color = color[z])
   
ax.set_ylabel("Y")
ax.set_xlabel("X")
ax.set_zlabel("Z")
ax.set_zlim(0, 14)
ax.view_init(20, 40)
ax.text(x = 4, y = 2, z = 12, s = "Last Histogram",
        bbox = dict(facecolor = "white"), alpha = 0.5,
        color = "red", fontsize = 15) 

ax.text(x = 4, y = 0, z = 12, s = "First Histogram",
        bbox = dict(facecolor = "grey"), alpha = 0.5,
        color = "white", fontsize = 15)
plt.show()

