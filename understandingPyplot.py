# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 12:22:23 2016

@author: pastahl
"""


import matplotlib.pyplot as plt


plt.scatter([1,3], [2,4], c='g', s=[50,100])
plt.show()
plt.scatter([1.5,2], [2.5,5], c='r')
plt.show()


plt.figure(1)
#kuva2=plt.figure(2)
#kuva = plt.add_subplot(111)
plt.scatter([0.5,1], [1.5,5], c='b', s=1000)
plt.scatter([0.5,1], [1.5,5], c='b', s=1000)
plt.show()