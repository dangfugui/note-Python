#!/usr/bin/python
# -*- coding:utf-8 -*-
import  numpy as np
import matplotlib.pyplot as plot
import re
if __name__ == '__main__':
    #outfile = open('D:/out.txt', 'a')
    #outfile.write(msg)
    infile = open('D:/in.txt','r')
    map = {}
    index = 0
    for line in infile:
        # if index>100:
        #     break
        # index += 1
        pattern = re.compile(r'\d\d:\d\d:\d\d')
        alist = pattern.findall(line)
        for k in alist:
            key = int(k[0])*10**5 + int(k[1])*10**4 + int(k[3])*10**3 + int(k[4])*10**2 + int(k[6])*10
            if key <99999:
                continue
            if map.has_key(key):
                map[key] = map[key]+1
            else:
                map[key]=1
    list =[]
    for (key,value) in map.items():
        list.append([key,value])
    list = sorted(list)
    list = np.array(list)

    print list
    plot.plot(list[:,0], list[:,1], 'r.', label='Logistic Loss', linewidth=5)
    #plot.plot(listkey, listValue, 'g*', label='Logistic Loss', linewidth=2)
    #plot.plot(x, y_1, 'g-', label='0/1 Loss', linewidth=2)
    # plot.plot(x, y_hinge, label='Hinge Loss', linewidth=2)
    plot.grid()
    plot.legend(loc='upper right')
    plot.show()
