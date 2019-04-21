# coding=utf-8
# tap du lieu su dung
import dataProcessing as dp
# thu vien ve cua python
import matplotlib.pyplot as plt
# thu vien sklearn cho ho tro knn
from sklearn.neighbors import KNeighborsClassifier
#Đánh giá
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
#tap du lieu training va testing
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(dp.data_CoLoc(0),dp.data_CoLoc(1),test_size=0.2)
x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(dp.data_khongLoc(0),dp.data_khongLoc(1),test_size=0.2)


                                # Tim nhung parameters tot nhat
# object luu param tot nhat
class good_KNN:
    def __init__(seft,weights,n_neighbors,F):
        seft.weights=weights
        seft.n_neighbors=n_neighbors
        seft.F=F
# tim  n_neighbors va weights tot nhat

def n_neighbors(k):
    n_neighbors=[]
    if k==0:
        for i in range(15):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==1:
        for i in range(15,30):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==2:
        for i in range(30,42):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==3:
        for i in range(42,50):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==4:
       for i in range(52,56):
          if i%2 !=0:
              n_neighbors.append(i)
    return n_neighbors
def timF_CoLoc(n,good_KNN_CoLoc):
    weights=['uniform','distance']
    knn = KNeighborsClassifier()
    param_grid = dict(n_neighbors=n, weights=weights)
    grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
    grid.fit(x_test_CoLoc, y_test_CoLoc)
# du lieu co loc
    clf=KNeighborsClassifier(n_neighbors=grid.best_estimator_.n_neighbors,weights=grid.best_estimator_.weights).fit(x_train_CoLoc,y_train_CoLoc)
    precision= precision_score(y_test_CoLoc,clf.predict(x_test_CoLoc), average='weighted')
    recall= recall_score(y_test_CoLoc,clf.predict(x_test_CoLoc), average='weighted')
    F_CoLoc=(2*precision*recall)/(precision+recall)
#so sanh
    if F_CoLoc>good_KNN_CoLoc.F:
            good_KNN_CoLoc=good_KNN(grid.best_estimator_.weights,
            grid.best_estimator_.n_neighbors,F_CoLoc)
            print("\t F_CoLoc=%s"%F_CoLoc)
    return good_KNN_CoLoc

def timF_KhongLoc(n,good_KNN_KhongLoc):
    weights=['uniform','distance']
    knn = KNeighborsClassifier()
    param_grid = dict(n_neighbors=n, weights=weights)
    grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
    grid.fit(x_test_CoLoc, y_test_CoLoc)
    #du lieu khong loc
    clf=KNeighborsClassifier(n_neighbors=grid.best_estimator_.n_neighbors,weights=grid.best_estimator_.weights).fit(x_train_KhongLoc,y_train_KhongLoc)
    precision= precision_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    recall= recall_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    F_KhongLoc=(2*precision*recall)/(precision+recall)
#so sanh
    if F_KhongLoc>good_KNN_KhongLoc.F:
            good_KNN_CoLoc=good_KNN(grid.best_estimator_.weights,
            grid.best_estimator_.n_neighbors,F_KhongLoc)
            print("\t  F_KhongLoc=%s "%F_KhongLoc)
    return good_KNN_CoLoc

def xuLy_knn_CoLoc():
    good_KNN_CoLoc=good_KNN(0,0,0)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(0),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(1),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(2),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(3),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(4),good_KNN_CoLoc)
    return good_KNN_CoLoc
def xuLy_knn_KhongLoc():
    good_KNN_KhongLoc=good_KNN(0,0,0)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(0),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(1),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(2),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(3),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(4),good_KNN_KhongLoc)
    return good_KNN_KhongLoc
def Ve(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe,ngauNhien):
    if len(mangCacDacTrungVe)>2:
             return False
    t=['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
         'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
         'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
         'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
         'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
         'so_luong_nhan_vien']
    m=[]
    for i in range(20):
        if t[i] in mangCacDacTrungVe:
            m.append(i)
    if chonBoDuLieu==0:
        mangVe=[]
        for i in range(soLuongDiemVe):
            mangVe.append([x_train_CoLoc[i][m[0]],x_train_CoLoc[i][m[1]],y_train_CoLoc[i]])
        plt.scatter(mangVe[0],mangVe[1],c=mangVe[2],label=mangVe[2])
        plt.show()
    elif chonBoDuLieu==1:
        mangVe=[]
        for i in range(soLuongDiemVe):
            mangVe.append([x_train_KhongLoc[i][m[0]],x_train_KhongLoc[i][m[1]],y_train_KhongLoc[i]])
        plt.scatter(mangVe[0],mangVe[1],c=mangVe[2],label=mangVe[2])
        plt.show()
def ketQua(k):
    if k==0:
        return xuLy_knn_CoLoc()
    elif k==1:
        return xuLy_knn_KhongLoc()
