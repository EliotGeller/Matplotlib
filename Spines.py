#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot()
data = []

for i in range (-5, 6):
    data.append(i)
    
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")   
ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
# (Position type, amount) "outward", "axes", "data"

ax.plot(data,data)
plt.show()

