# coding=utf-8
import sys
sys.path.append('../DAO/')
# tap du lieu su dung
import dataProcessing as dp
# thu vien ve cua python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# thu vien sklearn cho ho tro knn
from sklearn.neighbors import KNeighborsClassifier
#Đánh giá
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
#xu ly matrix
import numpy as np
#tap du lieu training va testing
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV
#sinh tổ hợp
from itertools import permutations



def sinhToHop(k):
    perm = permutations(['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
    'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
    'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
    'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
    'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
    'so_luong_nhan_vien'],k)
    array=[]
    for i in list(perm):
         array.append(i)
    return array
class nhungDacTrungTotNhat:
    def __init__(seft,array,F):
        seft.array=array
        seft.F=F

def NhungDacTrungTotNhat(k):
    NDTTN=nhungDacTrungTotNhat(0,0)
    for i in range(10):
        x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(
        dp.data_khongLoc(0,sinhToHop(k)[i]),dp.data_khongLoc(1,None),test_size=0.2)
        clf=KNeighborsClassifier(n_neighbors=13).fit(x_train_KhongLoc,y_train_KhongLoc)
        precision= precision_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
        recall= recall_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
        F_KhongLoc=(2*precision*recall)/(precision+recall)
        if F_KhongLoc>NDTTN.F:
            NDTTN.array=sinhToHop(k)[i]
            NDTTN.F=F_KhongLoc
    return NDTTN

def timNhungDacTrungTotNhat():
    NDTTN=nhungDacTrungTotNhat(0,0)
    for i in range(3,10):
        tmp=NhungDacTrungTotNhat(i)
        if tmp.F>NDTTN.F:
            NDTTN.array=tmp.array
            NDTTN.F=tmp.F
    x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(
    dp.data_khongLoc(0,None,dp.data_khongLoc(1,None),test_size=0.2)
    clf=KNeighborsClassifier(n_neighbors=13).fit(x_train_KhongLoc,y_train_KhongLoc)
    precision= precision_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    recall= recall_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    F_KhongLoc=(2*precision*recall)/(precision+recall)
    if F_KhongLoc>NDTTN.F:
        NDTTN.array=None
        NDTTN.F=F_KhongLoc
    return NDTTN


#tap du lieu
x_train_CoLoc, x_test_CoLoc, y_train_CoLoc, y_test_CoLoc=train_test_split(
dp.data_CoLoc(0,timNhungDacTrungTotNhat().array),
dp.data_CoLoc(1,None),
test_size=0.1)

x_train_KhongLoc, x_test_KhongLoc, y_train_KhongLoc, y_test_KhongLoc=train_test_split(
dp.data_khongLoc(0,timNhungDacTrungTotNhat().array),
dp.data_khongLoc(1,None),test_size=0.2)



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
    elif k==5:
           for i in range(56,100):
              if i%2 !=0:
                  n_neighbors.append(i)
    return n_neighbors
# tim F cho tap du lieu co loc
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
    return good_KNN_CoLoc

# tim F cho tap du lieu khong loc
def timF_KhongLoc(n,good_KNN_KhongLoc):
    weights=['uniform','distance']
    knn = KNeighborsClassifier()
    param_grid = dict(n_neighbors=n, weights=weights)
    grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
    grid.fit(x_test_KhongLoc, y_test_KhongLoc)
    #du lieu khong loc
    clf=KNeighborsClassifier(n_neighbors=grid.best_estimator_.n_neighbors,weights=grid.best_estimator_.weights).fit(x_train_KhongLoc,y_train_KhongLoc)
    precision= precision_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    recall= recall_score(y_test_KhongLoc,clf.predict(x_test_KhongLoc), average='weighted')
    F_KhongLoc=(2*precision*recall)/(precision+recall)
#so sanh
    if F_KhongLoc>good_KNN_KhongLoc.F:
            good_KNN_KhongLoc=good_KNN(grid.best_estimator_.weights,
            grid.best_estimator_.n_neighbors,F_KhongLoc)
    return good_KNN_KhongLoc

#Xu ly tinh toan cho tap du lieu co loc
def xuLy_knn_CoLoc():
    good_KNN_CoLoc=good_KNN(0,0,0)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(0),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(1),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(2),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(3),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(4),good_KNN_CoLoc)
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(5),good_KNN_CoLoc)
    return good_KNN_CoLoc
#Xu ly tinh toan cho tap du lieu khong loc
def xuLy_knn_KhongLoc():
    good_KNN_KhongLoc=good_KNN(0,0,0)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(0),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(1),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(2),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(3),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(4),good_KNN_KhongLoc)
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(5),good_KNN_KhongLoc)
    return good_KNN_KhongLoc

def ketQua(k):
    if k==0:
        return xuLy_knn_CoLoc()
    elif k==1:
        return xuLy_knn_KhongLoc()





                                #Ve



#tra ve vi tri cac dac trung cung cap cho ham ve
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

#ve 2 dac trung trong cac dac trung
def Ve2D(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe):
    if soLuongDiemVe>len(x_train_CoLoc) and chonBoDuLieu==0:
        return None
    if soLuongDiemVe>len(x_train_KhongLoc) and chonBoDuLieu==1:
        return None
    if len(mangCacDacTrungVe)!=2:
             return False
    m=[]
    for i in mangCacDacTrungVe:
        if traSoThuTu(i)!=-1:
            m.append(traSoThuTu(i))
    mangVe0=[]
    mangVe1=[]
    if chonBoDuLieu==0:
        for i in range(soLuongDiemVe):
            if y_train_CoLoc[i] ==0:
                mangVe0.append([x_train_CoLoc[i][m[0]],x_train_CoLoc[i][m[1]],y_train_CoLoc[i]])
            elif y_train_CoLoc[i]==1:
                mangVe1.append([x_train_CoLoc[i][m[0]],x_train_CoLoc[i][m[1]],y_train_CoLoc[i]])
    elif chonBoDuLieu==1:
        for i in range(soLuongDiemVe):
            if y_train_KhongLoc[i]==0:
                mangVe0.append([x_train_KhongLoc[i][m[0]],x_train_KhongLoc[i][m[1]],y_train_KhongLoc[i]])
            elif y_train_KhongLoc[i]==1:
                mangVe1.append([x_train_KhongLoc[i][m[0]],x_train_KhongLoc[i][m[1]],y_train_KhongLoc[i]])
    mangVe0=np.array(mangVe0)
    mangVe1=np.array(mangVe1)
    plt.scatter(mangVe0[:,0],mangVe0[:,1],marker="x",label="Thất bại",s=100)
    plt.scatter(mangVe1[:,0],mangVe1[:,1],marker="*",label="Thành công",s=100)
    plt.xlabel(mangCacDacTrungVe[0])
    plt.ylabel(mangCacDacTrungVe[1])
    plt.title("Biểu đồ phân 2 lớp sử dụng knn")
    plt.legend(loc='upper left')
    plt.show()


def Ve3D(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe):
    if soLuongDiemVe>len(x_train_CoLoc) and chonBoDuLieu==0:
        return None
    if soLuongDiemVe>len(x_train_KhongLoc) and chonBoDuLieu==1:
        return None
    if len(mangCacDacTrungVe)!=3:
             return False
    m=[]
    for i in mangCacDacTrungVe:
        if traSoThuTu(i)!=-1:
            m.append(traSoThuTu(i))
    mangVe0=[]
    mangVe1=[]
    if chonBoDuLieu==0:
        for i in range(soLuongDiemVe):
            if y_train_CoLoc[i] ==0:
                mangVe0.append([x_train_CoLoc[i][m[0]],x_train_CoLoc[i][m[1]],x_train_CoLoc[i][m[2]],y_train_CoLoc[i]])
            elif y_train_CoLoc[i]==1:
                mangVe1.append([x_train_CoLoc[i][m[0]],x_train_CoLoc[i][m[1]],x_train_CoLoc[i][m[2]],y_train_CoLoc[i]])
    elif chonBoDuLieu==1:
        for i in range(soLuongDiemVe):
            if y_train_KhongLoc[i]==0:
                mangVe0.append([x_train_KhongLoc[i][m[0]],x_train_KhongLoc[i][m[1]],x_train_KhongLoc[i][m[2]],y_train_KhongLoc[i]])
            elif y_train_KhongLoc[i]==1:
                mangVe1.append([x_train_KhongLoc[i][m[0]],x_train_KhongLoc[i][m[1]],x_train_KhongLoc[i][m[2]],y_train_KhongLoc[i]])
    mangVe0=np.array(mangVe0)
    mangVe1=np.array(mangVe1)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mangVe0[:,0],mangVe0[:,1],mangVe0[:,2],marker="x",label="Thất bại",s=100)
    ax.scatter(mangVe1[:,0],mangVe1[:,1],mangVe1[:,2],marker="*",label="Thành công",s=100)
    ax.set_xlabel(mangCacDacTrungVe[0])
    ax.set_ylabel(mangCacDacTrungVe[1])
    ax.set_zlabel(mangCacDacTrungVe[2])
    plt.title("Biểu đồ phân 2 lớp sử dụng knn")
    plt.legend(loc='lower left')
    plt.show()


                                #help

def help():
    print("\nhelp:\t\t.Ve2D(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe)\n")
    print("\t\t.Ve3D(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe)\n")
    print("\t\t\tchonBoDuLieu: 0 -> du lieu co Loc\n")
    print("\t\t\t              1 -> du lieu khong Loc\n")
    print("\t\t.ketQua(k) tra ve gia tri F voi k: 0 -> du lieu co Loc\n")
    print("\t\t                                k: 1 -> du lieu khong Loc\n")
