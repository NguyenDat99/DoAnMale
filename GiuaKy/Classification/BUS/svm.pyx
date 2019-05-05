import sys
sys.path.append('../DAO/')
# thoi gian
import datetime
# tap du lieu su dung
import dataProcessing as dp
# thu vien ve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# danh gia do chinh xac
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
# xu ly matrix
import numpy as np
# svm
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV

x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0,None),dp.data_CoLoc(1,None),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0,None),dp.data_khongLoc(1,None),test_size=0.2)

'''-------------------------------------test SVC với c = 1, kernel = linear '''
''' data có lọc '''
def svcloc():
    clf = SVC(C=1, kernel='linear')
    clf.fit(x_train_CoLoc,y_train_CoLoc)
    y_pred =  clf.predict(x_test_CoLoc)
    print('\nAccuracy = ',accuracy_score(y_test_CoLoc, y_pred))
    print('\nClassification report\n')
    print(classification_report(y_test_CoLoc, y_pred))
''' data không lọc '''
def svckloc():
    clf = SVC(C=1, kernel='linear')
    clf.fit(x_train_KhongLoc,y_train_KhongLoc)
    y_pred =  clf.predict(x_test_KhongLoc)
    print('\nAccuracy = ',accuracy_score(y_test_KhongLoc, y_pred))
    print('\nClassification report\n')
    print(classification_report(y_test_KhongLoc, y_pred))
'''----------------------------------------------------------test LinearSVC'''
''' data có lọc '''
def linearloc():
    clf = LinearSVC(random_state = 0, tol = 1e-5)
    clf.fit(x_train_CoLoc,y_train_CoLoc)
    y_pred =  clf.predict(x_test_CoLoc)
    print('\nAccuracy = ',accuracy_score(y_test_CoLoc, y_pred))
    print('\nClassification report\n')
    print(classification_report(y_test_CoLoc, y_pred))
''' data không lọc '''
def linearkloc():
    clf = LinearSVC(random_state = 0, tol = 1e-5)
    clf.fit(x_train_KhongLoc,y_train_KhongLoc)
    y_pred =  clf.predict(x_test_KhongLoc)
    print('\nAccuracy = ',accuracy_score(y_test_KhongLoc, y_pred))
    print('\nClassification report\n')
    print(classification_report(y_test_KhongLoc, y_pred))

'''--------------------------------------------------------test gridsearch '''
def gridsvc():
    clf = [{'C': [0.001, 0.01, 0.1, 1]}]
    grid = GridSearchCV(SVC(), clf, n_jobs=-1, cv = 5)
    grid.fit(x_train_CoLoc, y_train_CoLoc)
    print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))
    
def gridsvc1():
    clf = [{'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1]}]
    grid = GridSearchCV(SVC(), clf, n_jobs=-1, cv = 5)
    grid.fit(x_train_CoLoc, y_train_CoLoc)
    print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))
    

print("\t\t\t 3 -> chương trình chạy xong lúc %s" %datetime.datetime.now())

