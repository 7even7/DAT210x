# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 15:51:23 2016

@author: pastahl
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

from sklearn.datasets import load_iris
from pandas.tools.plotting import andrews_curves

student_dataset = pd.read_csv('C:\Data\Projektit\DAT210x\Datasets\students.data', index_col=0)
my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2','G1']]

# Histograms
my_series.plot.hist(alpha=0.5)
#my_dataframe.plot.hist(alpha=0.2, normed=True)
#my_dataframe.plot.hist(alpha=0.2)
#age_series = student_dataset.age

# 2D Scatter Plots
#student_dataset.plot.scatter(x='G1',y='G3')

# 3D Scatter plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset['Dalc'], c='r',marker='.')
#plt.show()



# Load up SKLearn's Iris Dataset into a Pandas Dataframe
#data = load_iris()
#df = pd.DataFrame(data.data, columns=data.feature_names)
#df['target_names'] = [data.target_names[i] for i in data.target]

# Andrews Curves Start Here:
#plt.figure()
#andrews_curves(df, 'target_names')
#plt.show()
