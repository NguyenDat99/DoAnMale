import pandas as pd
import numpy
import dataProcessing as dp
from scipy.integrate._ivp.radau import C
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
#----------------------------------------------------------------------
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.5)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.5)
#tim gamma tốt nhất
gammaArr = []
accurArr = []
for i in range(1,10):
    val = i / 10
    gammaArr.append(val)
for val in gammaArr:
    SVM = SVC(kernel = 'rbf', degree = 3, gamma = val, coef0 = 1)
    SVM.fit(x_train_KhongLoc, y_train_KhongLoc)
    predicting_label = SVM.predict(x_test_KhongLoc)
    accurArr.append(metrics.accuracy_score(y_test_KhongLoc, predicting_label))

plt.plot(gammaArr, accurArr, color='green', marker='.', linestyle='dashed',
         linewidth=1, markersize=8)
plt.xlabel('Gamma')
plt.ylabel('Accuracy')
plt.show()






