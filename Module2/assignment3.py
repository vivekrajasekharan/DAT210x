import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
#['motor'0, 'screw'1, 'pgain'2, 'vgain'3, 'class'4]
df=pd.read_csv('D:/Python_Microscoft/DAT210x/Module2/Datasets/servo.data',index_col=False, header=None)
df.head(5)
#E,E,5,4, 0.28125095
#B,D,6,5, 0.5062525
#D,D,4,3, 0.35625148
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
df2=df[df.iloc[:,3]==5]
print (len(df2)) #22
# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
df3=df[(df.iloc[:,0]=='E') & (df.iloc[:,1]=='E') ]
len(df3) #6

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
df4=df[df.iloc[:,2]==4]
df4.iloc[:,3].describe() #2.060606

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



