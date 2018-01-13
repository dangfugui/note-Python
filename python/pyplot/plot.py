#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = [10,    11,     12,  13,    14]
y = [0.8, 0.9   ,0.8,0.9,   1]
xx = [10,    11,     12,  13,    14]
yy = [0.7, 0.7   ,0.9,0.9,   1]

plt.figure()
plt.plot(x, y, 'r')
plt.plot(xx, yy, 'g')
plt.xlabel("time(s)")
plt.ylabel("value(m)")
plt.ylim(0, 1)
plt.xlim(10, 14)
plt.grid(True)
plt.title(u'2010金融')
plt.show()