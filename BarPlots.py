#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import randint

group1 = []
Index = []
group1err = []
ident = ["Value 1","Value 2","Value 3","Value 4","Value 5"]
group2 = []
group2err = []


for i in range(5):
    group1.append(randint(30,40))
    group2.append(randint(30,40))
    group1err.append(randint(1,5))
    group2err.append(randint(1,5))
    Index.append(i)
 
plt.figure(figsize = (10,8))
plt.bar(Index, group1, width = 0.5, color= ["red","green"], 
        edgecolor = "black", linewidth = 2, yerr = group1err,
        ecolor = "black", tick_label = ident, align = "center",
        log = False)
plt.bar(Index, group2, width = 0.5, align = "center", bottom = group1,
        edgecolor = "black", linewidth = 2, yerr = group2err, 
        ecolor = "black")
plt.show()

