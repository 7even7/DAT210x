import pandas as pd
import matplotlib.pyplot as plt
import matplotlib



# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv('C:\Data\Projektit\DAT210x\Module3\Datasets\wheat.data', index_col=0)

#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
# .. your code here ..
s1 = df[["area","perimeter"]]
plt.scatter(s1['area'], s1['perimeter'])
plt.title("AREA vs PERIMETER")
plt.ylabel("Perimeter")
plt.xlabel("Area")
plt.show()



# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..
plt.scatter(df["groove"], df["asymmetry"])
plt.title("GROOVE vs ASYMMETRY")
plt.show()

#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# .. your code here ..
plt.scatter(df['compactness'], df['width'], marker = '8')
plt.title("COMPACTNESS vs WIDTH")
plt.show()


# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


