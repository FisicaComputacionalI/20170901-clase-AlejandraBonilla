# lineplot.py 
import numpy as np
import pylab as pl 
# Make an array of x values
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# Make an array of y values fro each x value
y = [0, 0, 0, 0, 1, 2, 1, 2, 3, 5, 20, 0  , 0, 0, 0  , 1, 1,   2, 2,   3, 3, 2]
# use pylab to plot x and y
pl.plot(x, y)
# show the plot on the screen 
pl.savefig('temp1.png')

