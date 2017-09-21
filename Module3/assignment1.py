import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df=pd.read_csv('D:\Python_Microscoft\DAT210x\Module3\Datasets\wheat.data',index_col=0, header=0)

df.head(5)

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
# .. your code here ..
s1=df.iloc[:,0:2]

#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
# .. your code here ..

s2=df.iloc[:,5:7]
#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..
plt.hist(s1.iloc[:,0], alpha =0.75)
plt.hist(s1.iloc[:,1], alpha =0.75)
plt.figure()
plt.hist(s2.iloc[:,0], alpha =0.75)
plt.hist(s2.iloc[:,1].dropna(), alpha =0.75)
# Display the graphs:
plt.show()

