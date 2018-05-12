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


for i in range(50):
    group1.append(float(randint(30,40)))
    group2.append(float(randint(30,40)))
    group1err.append(float(randint(1,5)))
    group2err.append(float(randint(1,5)))
    Index.append(i)
 
plt.stackplot(Index, group1, group2, group1err, group2err,
              labels = ["Data 1", "Data 2", "Data 1 err", "Data 2 err"],
              colors = ["red", "blue", "green", "pink"],
              baseline = 'weighted_wiggle')
plt.legend(loc = 'lower right')
plt.show()