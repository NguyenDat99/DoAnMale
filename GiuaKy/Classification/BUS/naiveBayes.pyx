import sys
sys.path.append('../DAO/')
# tap du lieu su dung
import dataProcessing as dp
# thoi gian
import datetime
# thu vien ve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# xu ly matrix
import numpy as np
# naive bayes
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
# tim param tot nhat
from sklearn.model_selection import GridSearchCV
# danh gia do chinh xac
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV

x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0,None),dp.data_CoLoc(1,None),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0,None),dp.data_khongLoc(1,None),test_size=0.2)

'''--------------------------------------------------------------GaussianNB'''
'''data có lọc'''
def gauloc():
    clf = GaussianNB()
    clf.fit(x_train_CoLoc,y_train_CoLoc)
    y_pred =  clf.predict(x_test_CoLoc)
    print('\nAccuracy GaussianNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
    print('\nClassification report GaussianNB (coloc) \n')
    print(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
def gaukloc():
    clf = GaussianNB()
    clf.fit(x_train_KhongLoc,y_train_KhongLoc)
    y_pred =  clf.predict(x_test_KhongLoc)
    print('\nAccuracy GaussianNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
    print('\nClassification report GaussianNB (khongloc) \n')
    print(classification_report(y_test_KhongLoc, y_pred))

'''-----------------------------------------------------------MultinomialNB'''
'''data có lọc'''
def mulloc():
    clf = MultinomialNB()
    clf.fit(x_train_CoLoc,y_train_CoLoc)
    y_pred =  clf.predict(x_test_CoLoc)
    print('\nAccuracy MultinomialNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
    print('\nClassification report MultinomialNB (coloc) \n')
    print(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
def mulkloc():
    clf = MultinomialNB()
    clf.fit(x_train_KhongLoc,y_train_KhongLoc)
    y_pred =  clf.predict(x_test_KhongLoc)
    print('\nAccuracy MultinomialNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
    print('\nClassification report MultinomialNB (khongloc) \n')
    print(classification_report(y_test_KhongLoc, y_pred))
'''-------------------------------------------------------------BernoulliNB'''
'''data có lọc'''
def berloc():
    clf = BernoulliNB()
    clf.fit(x_train_CoLoc,y_train_CoLoc)
    y_pred =  clf.predict(x_test_CoLoc)
    print('\nAccuracy BernoulliNB (coloc) = ',accuracy_score(y_test_CoLoc, y_pred))
    print('\nClassification report BernoulliNB (coloc) \n')
    print(classification_report(y_test_CoLoc, y_pred))
'''data không lọc'''
def berkloc():
    clf = BernoulliNB()
    clf.fit(x_train_KhongLoc,y_train_KhongLoc)
    y_pred =  clf.predict(x_test_KhongLoc)
    print('\nAccuracy BernoulliNB (khongloc) = ',accuracy_score(y_test_KhongLoc, y_pred))
    print('\nClassification report BernoulliNB (khongloc) \n')
    print(classification_report(y_test_KhongLoc, y_pred))

print("\t\t\t 3 -> Chương trình chạy xong lúc %s" %datetime.datetime.now())
