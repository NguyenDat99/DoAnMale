import datetime
import dataProcessing as dp
import matplotlib.pyplot as plt
from scipy.integrate._ivp.radau import C
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import numpy as np
from matplotlib.colors import  ListedColormap
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVC
#Đánh giá
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV

x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.2)

# test với c = 1, kernel = linear
# data có lọc
clf = SVC(C=1, kernel='linear')
clf.fit(x_train_CoLoc,y_train_CoLoc)
accuracy = clf.score(x_test_CoLoc,y_test_CoLoc)
y_pred =  clf.predict(x_test_CoLoc)
cm = confusion_matrix(y_test_CoLoc, y_pred)
print('\nAccuracy : \n')
print(accuracy)
print('\nClassification report\n')
print(classification_report(y_test_KhongLoc, y_pred))
# data không lọc
clf = SVC(C=1, kernel='linear')
clf.fit(x_train_KhongLoc,y_train_KhongLoc)
accuracy = clf.score(x_test_KhongLoc,y_test_KhongLoc)
y_pred =  clf.predict(x_test_KhongLoc)
cm = confusion_matrix(y_test_KhongLoc, y_pred)
print('\nAccuracy : \n')
print(accuracy)
print('\nClassification report\n')
print(classification_report(y_test_KhongLoc, y_pred))

#test gridsearch
#clf = [{'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1]}]
#clf = [{'C': [0.001, 0.01, 0.1, 1]}]
#grid = GridSearchCV(SVC(), clf, n_jobs=-1, cv = 5)
#grid.fit(x_train_CoLoc, y_train_CoLoc)
#print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))

# Feature Scaling
#sc = StandardScaler()
#x_train_CoLoc = sc.fit_transform(x_train_CoLoc)
#x_test_CoLoc = sc.transform(x_test_CoLoc)
# Fitting SVM to the Training set using Kernel as linear.
#classifier = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#  decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
#  max_iter=-1, probability=False, random_state=0, shrinking=True,
#  tol=0.001, verbose=False)
#classifier.fit(x_train_CoLoc,y_train_CoLoc)
#accuracy = classifier.score(x_test_CoLoc,y_test_CoLoc)
#y_pred =  classifier.predict(x_test_CoLoc)
#cm = confusion_matrix(y_test_CoLoc, y_pred)

# Visualising the Training set results
#X_set, Y_set = x_train_CoLoc, y_train_CoLoc
#X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
#plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
#plt.xlim(X1.min(), X1.max())
#plt.ylim(X2.min(), X2.max())
#for i, j in enumerate(np.unique(Y_set)):
#    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
#                c = ListedColormap(('red','green'))(i),label = j)
#plt.title('SVM (Training set)')
#plt.legend()
#print('\nAccuracy : \n')
#print(accuracy)
#print('\nClassification report\n')
#print(classification_report(y_test_CoLoc, y_pred))
#plt.show()

print("\t\t\t 3 -> chương trình chạy xong lúc %s" %datetime.datetime.now())

