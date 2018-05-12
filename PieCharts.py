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
    group1.append(float(randint(30,40)))
    group2.append(float(randint(30,40)))
    group1err.append(float(randint(1,5)))
    group2err.append(float(randint(1,5)))
    Index.append(i)
 
plt.pie(group1, labels = ident, explode = [0.1,0,0,0,0], 
        colors = ["red", "blue", "green", "orange", "pink"],
        labeldistance = 1.2,
        shadow = True, startangle = None, counterclock = True,
#       frame = True, radius = 0.3, center = (0.5,0.5)
        )
plt.show()