import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
names = ['motor', 'screw', 'pgain', 'vgain', 'class']
df = pd.read_csv('c:/Data/Projektit/DAT210x/Module2/Datasets/servo.data', names=names )
print df.head()

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
entriesWith5vgain=df[df['vgain']==5]
print "entries having a vgain equal to 5: " + str( len(entriesWith5vgain))



# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
entriesWithMotorandScrewE=df[(df['motor']=='E') & (df['screw']=='E')]
print "Entries having a motor equal to E and screw equal to E: "+ str(len(entriesWithMotorandScrewE))

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

print "Mean vgain of Entries with pgain=4"
print df[df['pgain']==4]['vgain'].mean()

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!

df.dtypes

