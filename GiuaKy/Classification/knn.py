# coding=utf-8
import dataProcessing as dp# tap du lieu su dung
import matplotlib.pyplot as plt # thu vien ve cua python
from sklearn.neighbors import KNeighborsClassifier # thu vien sklearn cho ho tro knn
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV
x_train, x_test, y_train, y_test=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.2)



class good_Knn:
    def __init__(seft,weights,algorithm,n_neighbors,p,metric):
        seft.weights=weights
        seft.algorithm=algorithm
        seft.n_neighbors=n_neighbors
        seft.p=p
        seft.metric=metric

weights=['uniform','distance']
n_neighbors=[]
for i in range(499):
    if i%2 !=0:
        n_neighbors.append(i+2)
knn = KNeighborsClassifier()
param_grid = dict(n_neighbors=n_neighbors, weights=weights)
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
grid.fit(x_test, y_test)
good_Knn=good_Knn(grid.best_estimator_.weights,grid.best_estimator_.algorithm,
grid.best_estimator_.n_neighbors,grid.best_estimator_.p,grid.best_estimator_.metric)
print(good_Knn.metric)
#























print("\t\t\t 3 ->  Xử lý thuật toán Knn thành công!")
