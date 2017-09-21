#
# TODO: Import whatever needs to be imported to make this work
#
# .. your code here ..
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Look Pretty
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'

def doKMeans(dfa):
  #
  # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

  #
  # TODO: Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  # .. your code here ..

  #
  # TODO: Use K-Means to try and find seven cluster centers in this df.
  # Be sure to name your kmeans model `model` so that the printing works.
  #

  # .. your code here ..
  kmeans = KMeans(n_clusters=7, random_state=None).fit(dfa)
#  kmeans.labels_
  labels = kmeans.predict(dfa)

  #
  # INFO: Print and plot the centroids...
  centroids = kmeans.cluster_centers_
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  print (centroids)



#
# TODO: Load your dataset after importing Pandas
#
# .. your code here ..
df= pd.read_csv("D:\Python_Microscoft\DAT210x\Module5\Datasets\Crimes.csv")



#
# TODO: Drop any ROWs with nans in them
#
# .. your code here ..
df=df.dropna()

  
df.reset_index(drop=True)
df2=df.loc[:,["Longitude", "Latitude"]]
#
# TODO: Print out the dtypes of your dset
#
# .. your code here ..


#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
# .. your code here ..


# INFO: Print & Plot your data
doKMeans(df2)


#
# TODO: Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
# .. your code here ..

df.Date=pd.to_datetime(df.Date)
df=df[df.Date>'2011-01-01 00:00:00']
df4=df.loc[:,["Longitude", "Latitude"]]
# INFO: Print & Plot your data
doKMeans(df4)
plt.show()


