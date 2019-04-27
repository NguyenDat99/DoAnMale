import dataProcessing as dp
import datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from mpl_toolkits.mplot3d import Axes3D
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.2)

'''--------------------------------------------------------------GaussianNB'''
'''data có lọc'''
#clf = GaussianNB()
#clf.fit(x_train_CoLoc,y_train_CoLoc)
#y_pred =  clf.predict(x_test_CoLoc)
#print('\nAccuracy GaussianNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
#print('\nClassification report GaussianNB (coloc) \n')
#print(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
#clf = GaussianNB()
#clf.fit(x_train_KhongLoc,y_train_KhongLoc)
#y_pred =  clf.predict(x_test_KhongLoc)
#print('\nAccuracy GaussianNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
#print('\nClassification report GaussianNB (khongloc) \n')
#print(classification_report(y_test_KhongLoc, y_pred))

'''-----------------------------------------------------------MultinomialNB'''
'''data có lọc'''
#clf = MultinomialNB()
#clf.fit(x_train_CoLoc,y_train_CoLoc)
#y_pred =  clf.predict(x_test_CoLoc)
#print('\nAccuracy MultinomialNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
#print('\nClassification report MultinomialNB (coloc) \n')
#print(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
#clf = MultinomialNB()
#clf.fit(x_train_KhongLoc,y_train_KhongLoc)
#y_pred =  clf.predict(x_test_KhongLoc)
#print('\nAccuracy MultinomialNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
#print('\nClassification report MultinomialNB (khongloc) \n')
#print(classification_report(y_test_KhongLoc, y_pred))
'''-------------------------------------------------------------BernoulliNB'''
'''data có lọc'''
#clf = BernoulliNB()
#clf.fit(x_train_CoLoc,y_train_CoLoc)
#y_pred =  clf.predict(x_test_CoLoc)
#rint('\nAccuracy BernoulliNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
#print('\nClassification report BernoulliNB (coloc) \n')
#rint(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
#clf = BernoulliNB()
#clf.fit(x_train_KhongLoc,y_train_KhongLoc)
#y_pred =  clf.predict(x_test_KhongLoc)
#print('\nAccuracy BernoulliNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
#rint('\nClassification report BernoulliNB (khongloc) \n')
#print(classification_report(y_test_KhongLoc, y_pred))

''' vẽ '''
x_column = dp.data_CoLoc(0) 
y_column = dp.data_CoLoc(1)
z_column = dp.data_CoLoc(2)

x =np.array(x_column)
y =np.array(y_column)
z =np.array(z_column)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[:,0], y[:,1], c = 'r', marker = 'o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.show()

print("\t\t\t 3 -> Chương trình chạy xong lúc %s" %datetime.datetime.now())