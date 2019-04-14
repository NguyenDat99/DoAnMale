import pandas as pd
import numpy
import dataProcaessing_SVMkernel as dp
from scipy.integrate._ivp.radau import C
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
#----------------------------------------------------------------------
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.3)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.3)
#tim gamma tốt nhất
# gammaArr = []
# accurArr = []
# for i in range(1,20):
#     val = i / 10
#     gammaArr.append(val)
# for val in gammaArr:
#     SVM = SVC(kernel = 'rbf', degree = 3, gamma = val, coef0 = 1)
#     SVM.fit(x_train_CoLoc, y_train_CoLoc)
#     predicting_label = SVM.predict(x_test_KhongLoc)
#     accurArr.append(metrics.accuracy_score(y_test_KhongLoc, predicting_label))
#
# plt.plot(gammaArr, accurArr, color='green', marker='.', linestyle='dashed',
#          linewidth=1, markersize=8)
# plt.xlabel('Gamma')
# plt.ylabel('Accuracy')
# plt.show()
#-------------------------------------------------------------------------------
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-4],
                     'C': [1, 10, 100]}]
# tuned_parameters = [{'kernel': ['linear'],
#                      'C': [1, 10, 100]}]
grid = GridSearchCV(SVC(), tuned_parameters, cv=5)
grid.fit(x_train_CoLoc, y_train_CoLoc)
print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))





