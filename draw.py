# coding: utf-8
import numpy as np
import pylab as pl

def DrawImage(xList, yList):
    pl.xlabel('day')
    pl.ylabel('download number')
    number = 0;
    for x in xList :
        pl.plot(x, yList[number])
        number = number + 1
    pl.show()