import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..

df=pd.read_csv('D:/Python_Microscoft/DAT210x/Module2/Datasets/NFL.csv',index_col=False)
# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
df2=df.dropna (thresh=4, axis=0)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df2.duplicated()
df3=df2.drop_duplicates()
# TODO: Get rid of the 'RK' column
#
# .. your code here ..

df4=df3.drop(['RK'], axis=1)
# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

df5=df4.reset_index(drop=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..

for i in range (2,16):
    df5.iloc[:, i]=pd.to_numeric(df5.iloc[:, i], errors='coerce')

df5.dtypes
df6=df5.dropna (thresh=4, axis=0)
df6=df6.reset_index(drop=True)
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
len(df6)
len(df6.PCT.unique())