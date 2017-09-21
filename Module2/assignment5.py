import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
df=pd.read_csv('D:/Python_Microscoft/DAT210x/Module2/Datasets/census.data',index_col=0, header=None)
df.head(5)


#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
df.columns=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']

df['capital-gain'].unique()

df2=df
df2['capital-gain']=pd.to_numeric(df2['capital-gain'], errors='coerce')

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
# .. your code here ..

df3=pd.get_dummies(df2['classification'])
len(df3[df3.iloc[:,0]==1]) # less than 22744
len(df3[df3.iloc[:,0]==0]) #greater than 6792
len(df3.iloc[:,1]) #total
#
# TODO:
# Print out your dataframe
#
# .. your code here ..


