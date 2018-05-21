#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize = (5, 6))
ax = plt.subplot(111, projection = "3d")

X, Y, Z = axes3d.get_test_data() #delta = 0.05


ax.plot_surface(X, Y, Z, rstride = 10, cstride = 10, 
                cmap = plt.get_cmap("winter"))
ax.view_init(20, 120)
plt.show()

