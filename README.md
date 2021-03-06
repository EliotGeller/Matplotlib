# Matplotlib
A couple of small Python files used to learn about the matplotlib library and some of its functions.

FirstScatter.py is my first time using matplotlib and pyplot.  It has a simple scatter plot and a few line plots used to understand how graph customization works using the library.

Histograms.py is my second matplotlib file where I explored some of the histogram features.

BarPlots.py is my third matplotlib file.  This went over similar method parameters from the previous files.

StackPlots.py tested the different baselines and weights in a stack plot of 4 data sets of random numbers.

PieCharts.py tested the included .pie parameters included in pyplot, such as colors, exploding, and rotation of a pie chart.

BoxAndWhisker.py was to learn about the caps, fliers, positions, etc. of a box and whisker plot created with pyplot.

FiguresAndSubplots.py expanded on BoxAndWhisker.py by adding extra subplots and figures to the existing code.

FinanceGraph.py used the seperately installed mpl_finance module that replaces the now deprecated matplotlib.finance library.  This code creates a candlestick graph from data parsed from a Yahoo finance csv file (AAPL.csv)

LiveGraph.py utilizes the FuncAnimation module from the matplotlib.animations to demonstrate an animated graph over time.

Styling.py used a simple linear graph to explore the different options included in matplotlib.style, matplotlib.rcParams, and the pyplot.xkcd style.

AxisSharing.py uses the twinx method to share the X-axis for 2 graphs on the same plot.

Spines.py used the built in .spines methods to manipulate how spines are visualized in graphs.

MultipleAxes.py uses the mpl_toolkits.axes_grid1 library to create multiple graphs on a single plot.  This specific example has a 2d histogram along with 2 bar-graphs and a scatter plot do show randomly created data.

First3D.py was my first look at 3D plotting using Axes3D from the mpl_toolkits.mplot3d library.

Surface.py is a very basic surface plot that also has options to change the colormap.

Wireframes.py plots three different graphs of wireframe graphs, and contour plots in addition to exploring how offsetting contour plots in a single subplot can give different visualizations.

HistoStack.py uses the mplot3d library to stack multiple histograms into one plot for data comparison.
