import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import glob
from sklearn.manifold import Isomap
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples=[]
colors=[]
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
for i in glob.glob('D:/Python_Microscoft/DAT210x/Module4/Datasets/ALOI/32/*.png'):
    img=misc.imread(i)
    img = img[::2, ::2]
    ll=img.reshape(-1)

    samples.append(ll)
    colors.append('b')
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for i in glob.glob('D:/Python_Microscoft/DAT210x/Module4/Datasets/ALOI/32i/*.png'):
    img=misc.imread(i)
    img = img[::2, ::2]
    ll=img.reshape(-1)

    samples.append(ll)
    colors.append('r')

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
df=pd.DataFrame(samples).T

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 

iso=Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T1=iso.transform(df)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 

plt.figure()
plt.scatter(T1[:,1], T1[:,2], marker='o', c=colors)


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.scatter(T1[:,0],T1[:,1], T1[:,2], marker='.', c=colors)


plt.show()

