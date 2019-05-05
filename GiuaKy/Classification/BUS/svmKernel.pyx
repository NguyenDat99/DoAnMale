import pandas as pd
import numpy as np
import sys
sys.path.append('../DAO/')
# tap du lieu su dung
import dataProcessing as dp
from sklearn.metrics import classification_report
from scipy.integrate._ivp.radau import C
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

#----------------------------------------------------------------------
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0,['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung','co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac','ngay_lien_lac','thoi_luong_lien_lac']),dp.data_CoLoc(1,None),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0,['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung','co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac','ngay_lien_lac','thoi_luong_lien_lac']),dp.data_khongLoc(1,None),test_size=0.2)
#-------------------------------------------------------------------------------
#tìm parameter tốt nhất
def ketQua():
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [0.001, 0.01,0.1,1],
                          'C': [0.01,0.1,1,10]}]
    grid = GridSearchCV(SVC(), tuned_parameters, cv=5)
    grid.fit(x_train_CoLoc, y_train_CoLoc)
    print("parameter tốt nhất có lọc %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))
    clf = SVC(kernel='rbf',gamma=0.01,C=10) # rbf Kernel
    clf.fit(x_train_CoLoc, y_train_CoLoc)
    y_pred = clf.predict(x_test_CoLoc)
    print("Accuracy:",metrics.accuracy_score(y_test_CoLoc, y_pred))
    #tìm parameter tốt nhất khong lọc
    grid1 = GridSearchCV(SVC(), tuned_parameters, cv=5)
    grid1.fit(x_train_KhongLoc, y_train_KhongLoc)
    print("parameter tốt nhất khong lọc %s with a score of %0.2f"% (grid1.best_params_, grid1.best_score_))
#vẽ visualize
def ve():
    X=dp.data_CoLoc(0,['tuoi','nghe_nghiep'])  # Lấy hai thuộc tính đầu tiên
    Y=dp.data_CoLoc(1,None)
    X=np.array(X)
    Y=np.array(Y)

    X_min, X_max = X[:, 0].min() - .5, X[: ,0].max() + .5
    Y_min, Y_max = X[: ,1].min() - .5, X[: ,1].max() + .5
    plt.figure(2, figsize=(8, 6))
    plt.clf()
    #Biểu diễn tập dữ liệu huấn luyện bằng đồ
    plt.scatter(X[:, 0], X[:,1], c=Y)
    plt.xlabel('tuoi')
    plt.ylabel('nghe_nghiep')

    plt.xlim(X_min, X_max)
    plt.ylim(Y_min, Y_max)
    plt.xticks(())
    plt.yticks(())

    plt.show()
