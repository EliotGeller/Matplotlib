#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import gauss

x1 = []
x2 = []

for i in range(1000):
    x1.append(gauss(10,2))
    x2.append(gauss(10,2))
    
fig = plt.figure(num = "One")
ax = plt.subplot(221)   #nrows,ncols,plot_number = nrows*ncols
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
ax.boxplot(x = (x1,x2), notch = False, sym = "b+", vert = True,
            whis = 1.5, usermedians = [None,9], positions = range(1,3),
            widths = [0.3, 0.1], labels = ["Group 1", "Group 2"],
            showcaps = True, showfliers = True, showmeans = True)
ax2.boxplot(x2)
ax3.boxplot(x1)
ax4.boxplot(x = (x2,x1))
plt.legend()
plt.show()

