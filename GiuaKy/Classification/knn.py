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
        for i in range(100):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==1:
        for i in range(100,200):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==2:
        for i in range(200,300):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==3:
        for i in range(300,400):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==4:
        for i in range(400,500):
            if i%2 !=0:
                n_neighbors.append(i)
    elif k==5:
        for i in range(500,600):
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
            print(u"\t\t tìm ra F_CoLoc mới")
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
            print(u"\t\t tìm ra F_KhongLoc mới")
    return good_KNN_CoLoc

def xuLy_knn_CoLoc():
    good_KNN_CoLoc=good_KNN(0,0,0)
    print("\t\t 1%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(0),good_KNN_CoLoc)
    print("\t\t 8%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(1),good_KNN_CoLoc)
    print("\t\t 16%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(2),good_KNN_CoLoc)
    print("\t\t 24%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(3),good_KNN_CoLoc)
    print("\t\t 32%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(4),good_KNN_CoLoc)
    print("\t\t 40%")
    good_KNN_CoLoc=timF_CoLoc(n_neighbors(5),good_KNN_CoLoc)
    return good_KNN_CoLoc
def xuLy_knn_KhongLoc():
    good_KNN_KhongLoc=good_KNN(0,0,0)
    print("\t\t 48%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(0),good_KNN_KhongLoc)
    print("\t\t 56%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(1),good_KNN_KhongLoc)
    print("\t\t 64%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(2),good_KNN_KhongLoc)
    print("\t\t 72%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(3),good_KNN_KhongLoc)
    print("\t\t 80%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(4),good_KNN_KhongLoc)
    print("\t\t 88%")
    good_KNN_KhongLoc=timF_KhongLoc(n_neighbors(5),good_KNN_KhongLoc)
    print("\t\t 96%")
    return good_KNN_KhongLoc
def ketQua(k):
    if k==0:
        return xuLy_knn_CoLoc()
    elif k==1:
        return xuLy_knn_KhongLoc()
def Ve(chonBoDuLieu,mangCacDacTrungVe,soLuongDiemVe,ngauNhien):
    if chonBoDuLieu==0:
        t=['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
        'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
        'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
        'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
        'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
        'so_luong_nhan_vien']
        mangVe=[]
        for i in len(t):
            if t[i] in mangCacDacTrungVe:
                mangVe.append(i)
        #if ngauNhien==0:
            #plt.scatter(x_train[:,0],x_train[:,1], c=y_train)
            #plt.scatter(x_test[:,0],x_test[:,1], c=y_test,s=100)
            #plt.xlabel("X")
            #plt.ylabel("Y")
            #plt.title("Phân loại 3 lớp!")
            #plt.show()
#ax1.scatter(x[:4], y[:4], s=10, c='b', marker="s", label='first')
# ax1.scatter(x[40:],y[40:], s=10, c='r', marker="o", label='second')

                                        #help()
def help():
    print(u"Cú pháp")
