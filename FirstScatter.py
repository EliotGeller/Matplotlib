
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x = []
y = []
yTwo = []

for i in range(-100, 101, 5):
    x.append(i)
    y.append(i)
    yTwo.append(2*i)
    
#plt.scatter(x, y, s = 15, c = "green", marker = "o")
#plt.scatter(x, yTwo, c = "red", marker = "+")
#plt.show
    
    
xAxisTicks = ["01/01/2016", "01/06/2016", "01/12/2016"]
yAxisTicks = ["morning", "lunch time", "afternoon", "dinner time", 
              "evening", "night"]
plt.figure(figsize = (10,8))    
plt.plot(x, y, c = "red", ls = "-", lw = 1, marker = "o", ms = 10, 
         fillstyle = "left", mfc = "blue", label = "Graph 1")
plt.plot(x,yTwo, c = "green", label = "Graph 2")
plt.xlabel("This is the x-axis", color = "red", fontsize = 15, 
           horizontalalignment = "center", verticalalignment = "top")
plt.ylabel("This is the y-axis", color = "green")
plt.title(r"This is the title$\frac{1}{2}$", color = "blue", fontsize = 25,
          verticalalignment = "bottom")
plt.legend(loc = "lower right")
#plt.xticks([-100,0,100], xAxisTicks, rotation = 45)
#plt.yticks([-200,-100,-50,50,100,200], yAxisTicks, rotation = 45)
#plt.text(-30, 125, "My first text", color = "orange", rotation = 0,
#         style = "italic", fontsize = 15, weight = "heavy",
#         bbox = dict(facecolor = "blue", alpha = 0.45)) #x,y,s

#plt.annotate(xy = (0,20), xytext = (-25,150), s = "Annotation", 
#             arrowprops = dict(width = 5, headwidth = 10, headlength = 10,
#                               shrink = 0.0, facecolor = "red"))
#plt.savefig("OurFirstFigure.pdf", facecolor = "orange")
plt.xscale('symlog')
plt.yscale('symlog', basey = 5, subsy = [2,3,4], linthreshy = 25,
           linscaley = 1)
plt.show