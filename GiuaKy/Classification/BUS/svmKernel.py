import pandas as pd
import numpy
import dataProcaessing_SVMkernel as dp
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
h = .02  # step size in the mesh
#----------------------------------------------------------------------
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.3)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.3)
#-------------------------------------------------------------------------------
#tìm parameter tốt nhất
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-4],
                     'C': [1, 10, 100]}]
grid = GridSearchCV(SVC(), tuned_parameters, cv=5)
grid.fit(x_train_CoLoc, y_train_CoLoc)
print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))

#vẽ visualize
def traSoThuTu(ten):
    t=['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
    'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
    'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
    'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
    'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
    'so_luong_nhan_vien']
    for i in range(len(t)):
        if t[i]==ten:
            return i;
    return -1;

X = dp.data_CoLoc(0) # Lấy hai thuộc tính đầu tiên
Y =dp.data_CoLoc(1)
print(X)
# X_min, X_max = X[:, 0].min() - .5, X[:, 0].max() + .5
# Y_min, Y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
# plt.figure(2, figsize=(8, 6))
# plt.clf()
# # Biểu diễn tập dữ liệu huấn luyện bằng đồ
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
# plt.xlabel('tuoi')
# plt.ylabel('nghenghiep')
#
# plt.xlim(X_min, X_max)
# plt.ylim(Y_min, Y_max)
# plt.xticks(())
# plt.yticks(())
# plt.show()






