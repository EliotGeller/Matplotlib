#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import gauss

x1 = []
x2 = []

for i in range(1000):
    x1.append(gauss(10,2))
    x2.append(gauss(10,2))
    
plt.boxplot(x = (x1,x2), notch = False, sym = "b+", vert = True,
            whis = 1.5, usermedians = [None,9], positions = range(1,3),
            widths = [0.3, 0.1], labels = ["Group 1", "Group 2"],
            showcaps = True, showfliers = True, showmeans = True)
plt.legend()
plt.show()

