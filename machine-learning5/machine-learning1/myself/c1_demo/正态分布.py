#!/usr/bin/python
# -*- coding:utf-8 -*-
import  numpy
import matplotlib.pyplot as plot
if __name__ == '__main__':
    # count = 100
    # u = numpy.random.uniform(0.0, 1.0, count)
    # for time in range(100):
    #     print u
    #     u += numpy.random.uniform(0.0,1.1,count)
    # u /= 100
    # plot.hist(u,80,facecolor = 'g' ,alpha = 0.7)
    # plot.grid(True)
    # plot.show()
    u = numpy.random.uniform(0.0, 1.0, 10000)
    times = 1000
    for time in range(times):
        u += numpy.random.uniform(0.0,1.0,10000)
    print len(u)
    u /= times
    plot.hist(u,80,facecolor ='g' ,alpha = 0.7)
    plot.grid(True)
    plot.show()