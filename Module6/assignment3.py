#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np
X=pd.read_csv("D:/Python_Microscoft/DAT210x/Module6/Datasets/parkinsons.data")
y=X.status.copy()
X.drop(labels=["status", "name"], axis=1, inplace=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.30, random_state =7)

from sklearn.svm import SVC
#model=SVC()
#model.fit(X_train, y_train)
#score=model.score(X_test, y_test)
#print(score)
from sklearn import preprocessing

X_train=preprocessing.StandardScaler().fit_transform(X_train)
X_test=preprocessing.StandardScaler().fit_transform(X_test)
##0.966101694915 Best score is 0.966101694915 for C, gamma =  1.95 , 0.098

#X_train=preprocessing.KernelCenterer().fit_transform(X_train)
#X_test=preprocessing.KernelCenterer().fit_transform(X_test)
#0.847457627119

#X_train=preprocessing.MinMaxScaler().fit_transform(X_train)
#X_test=preprocessing.MinMaxScaler().fit_transform(X_test)
##0.881355932203

#X_train=preprocessing.MaxAbsScaler().fit_transform(X_train)
#X_test=preprocessing.MaxAbsScaler().fit_transform(X_test)
#0.881355932203

#X_train=preprocessing.Normalizer().fit_transform(X_train)
#X_test=preprocessing.Normalizer().fit_transform(X_test)
#0.796610169492

#Normalizer(), MaxAbsScaler(), MinMaxScaler(), KernelCenterer(), and StandardScaler().

Test_PCA = True
model = None
if Test_PCA:
  print ("2D PCA")

  from sklearn.decomposition import PCA
  model=PCA(n_components=15).fit(X_train)
  
  

else:
  print (" 2D Isomap Manifold")

  from sklearn.manifold import Isomap
  model=Isomap(n_neighbors=8, n_components=2).fit(X_train)

X_train=model.transform(X_train)
X_test=model.transform(X_test)

best_score=0
C=np.arange(0.05, 2.05, 0.05)
GAMMA=np.arange(0.001,0.1,0.001)
for c in C:
    for gamma in GAMMA:
        svc=SVC(C=c, gamma=gamma).fit(X_train, y_train)
        scored=svc.score(X_test, y_test)
        if scored > best_score:
            best_score=scored
            print ("Best score so far is", best_score, "for C, gamma = ", c,",", gamma)