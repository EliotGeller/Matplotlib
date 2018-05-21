#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize = (6,10))
ax = plt.subplot(311, projection = '3d')
ax2 = plt.subplot(312, projection = '3d')
ax3 = plt.subplot(313, projection = '3d')

X, Y, Z = axes3d.get_test_data() #delta = 0.05

ax.plot_wireframe(X, Y, Z, rstride = 5, cstride = 5)
#ax.view_init(40, 180)

ax2.contour(X, Y, Z)
#ax2.view_init(90, 20)

ax3.plot_wireframe(X, Y, Z, rstride = 10, cstride = 10)
ax3.contour(X, Y, Z, offset = -90)
ax3.contour(X, Y, Z, zdir = 'y', offset = 50)
ax3.contour(X, Y, Z, zdir = 'x', offset = -50)

ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_zlabel("z")
ax3.set_ylim(-50, 50)
ax3.set_zlim(-90, 90)
ax3.set_xlim(-50, 50)
#ax3.view_init(90,0)
plt.show()
