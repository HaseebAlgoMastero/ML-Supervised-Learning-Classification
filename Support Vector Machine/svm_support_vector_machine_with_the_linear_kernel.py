# -*- coding: utf-8 -*-
"""SVM Support Vector Machine with the Linear Kernel

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LEOd6_UyaW2t557FPbxnjq01ttXMG3zb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ads.csv')
x = df.iloc[:,0:2].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear',random_state = 0)
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)
score

from matplotlib.colors import ListedColormap
x_set ,y_set = sc.inverse_transform(x_train),y_train
X1,X2 = np.meshgrid(np.arange(start = x_set[:,0].min()-10,stop = x_set[:,0].max()+10,step = 1),
                   np.arange(start = x_set[:,1].min()-1000,stop = x_set[:,1].max()+1000,step = 1))
c1 = np.ravel(X1).reshape(-1,1)
c2 = np.ravel(X2).reshape(-1,1)
c3 = np.concatenate((c1,c2),axis = 1)
c4 = classifier.predict(sc.transform(c3))
plt.contourf(X1,X2,c4.reshape(X1.shape),alpha = 0.75,cmap = ListedColormap(('salmon', 'dodgerblue')))
colors = ListedColormap(('salmon', 'dodgerblue'))
unique_labels = np.unique(y_train)
for i in range(len(unique_labels)):
  labels = unique_labels[i]
  indices = np.where(y_train == labels)
  x_values = x_set[indices,0]
  y_values = x_set[indices,1]
  color = colors(i)
  plt.scatter(x_values,y_values, label = labels, c = color)
plt.legend()
plt.colorbar()
plt.show()

from matplotlib.colors import ListedColormap
x_set ,y_set = sc.inverse_transform(x_test),y_test
X1,X2 = np.meshgrid(np.arange(start = x_set[:,0].min()-10,stop = x_set[:,0].max()+10,step = 1),
                   np.arange(start = x_set[:,1].min()-1000,stop = x_set[:,1].max()+1000,step = 1))
c1 = np.ravel(X1).reshape(-1,1)
c2 = np.ravel(X2).reshape(-1,1)
c3 = np.concatenate((c1,c2),axis = 1)
c4 = classifier.predict(sc.transform(c3))
plt.contourf(X1,X2,c4.reshape(X1.shape),alpha = 0.75,cmap = ListedColormap(('salmon', 'dodgerblue')))
colors = ListedColormap(('salmon', 'dodgerblue'))
unique_labels = np.unique(y_test)
for i in range(len(unique_labels)):
  labels = unique_labels[i]
  indices = np.where(y_test == labels)
  x_values = x_set[indices,0]
  y_values = x_set[indices,1]
  color = colors(i)
  plt.scatter(x_values,y_values, label = labels, c = color)
plt.legend()
plt.colorbar()
plt.show()