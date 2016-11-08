import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv('C:\Data\Projektit\DAT210x\Module3\Datasets\wheat.data', index_col=0)

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..
#df.drop('id', axis=1, inplace=True)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
correlation = df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
#plt.matshow(correlation)

#plt.show()


plt.imshow(correlation, cmap=plt.cm.Blues, interpolation='nearest')
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)
plt.colorbar()
plt.show()


