# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 16:28:38 2016

@author: pastahl
"""
import matplotlib.pyplot as plt



student_dataset = pd.read_csv('C:\Data\Projektit\DAT210x\Datasets\students.data', index_col=0)
my_dataframe = student_dataset[['G3', 'G2','G1']]

plt.imshow(my_dataframe.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(my_dataframe.columns))]
plt.xticks(tick_marks, my_dataframe.columns, rotation='vertical')
plt.yticks(tick_marks, my_dataframe.columns)
plt.show()              