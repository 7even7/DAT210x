import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
url = "http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2"
df = pd.read_html(url, header = 1)[0]

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
df.columns = [
    "RK"
    ,"PLAYER"
    ,"TEAM"
    ,"GamesPlayed"
    ,"Goals"
    ,"Assists"
    ,"Points"
    ,"PlusMinusRating"
    ,"PenaltyMinutes"
    ,"PointsPerGame"
    ,"ShotsonGoal"
    ,"ShootingPercentage"
    ,"GameWinningGoals"
    ,"PowerPlayGoals"
    ,"PowerPlayAssists"
    ,"ShortHandedGoals"
    ,"ShortHandedAssists"]

df.GamesPlayed = pd.to_numeric(df.GamesPlayed, errors='coerce')
df.Goals = pd.to_numeric(df.Goals, errors='coerce')
df.Assists = pd.to_numeric(df.Assists, errors='coerce')
df.Points = pd.to_numeric(df.Points, errors='coerce')
df.PlusMinusRating = pd.to_numeric(df.PlusMinusRating, errors='coerce')
df.PenaltyMinutes = pd.to_numeric(df.PenaltyMinutes, errors='coerce')
df.PointsPerGame = pd.to_numeric(df.PointsPerGame, errors='coerce')
df.ShotsonGoal = pd.to_numeric(df.ShotsonGoal, errors='coerce')
df.ShootingPercentage = pd.to_numeric(df.ShootingPercentage, errors='coerce')
df.GameWinningGoals = pd.to_numeric(df.GameWinningGoals, errors='coerce')
df.PowerPlayGoals = pd.to_numeric(df.PowerPlayGoals, errors='coerce')
df.PowerPlayAssists = pd.to_numeric(df.PowerPlayAssists, errors='coerce')
df.ShortHandedGoals = pd.to_numeric(df.ShortHandedGoals, errors='coerce')
df.ShortHandedAssists = pd.to_numeric(df.ShortHandedAssists, errors='coerce')
print df.dtypes
# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
print df[df.iloc[:,0]>1]

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df=df.drop(labels=['RK'],axis=1 )

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

print df.dtypes

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
df.describe()
len(df)
len(df.ShootingPercentage.unique())
sum(df.loc[15:16,"GamesPlayed"])