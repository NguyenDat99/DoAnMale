import dataProcessing as dp
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def lay_data():
    data=dp.dataset(['luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi'])
    return data

def KMean(mangCacDacTrung,n_clusters):
    data=[]
    if mangCacDacTrung is None:
        data=dp.dataset(['luong_hao_xang',
        'so_luong_xi_lanh','the_tich_dong_co',
        'ma_luc','ty_le_truc_sau','khoi_luong_xe',
        'gia_toc_xe','loai_xy_lanh_dong_co',
        'loai_truyen_dong','so_luong_banh_rang',
        'so_luong_bo_che_hoa_khi'])
    else:
        data=dp.dataset(mangCacDacTrung)
    kmeans = KMeans(init='k-means++',n_clusters=n_clusters, random_state=0).fit(data)
    return kmeans


def veTimSoCluster(mangCacDacTrung,diemBatDau,diemKetThuc):
    clusters=[]
    for i in range(diemBatDau,diemKetThuc):
        kmeans = KMean(mangCacDacTrung,i)
        clusters.append([i,kmeans.inertia_])
    clusters=np.array(clusters)
    plt.plot(clusters[:,0],clusters[:,1],'-o',c='g',marker="+")
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.title("Biểu đồ phân tích Kmeans ")
    plt.show()

def traSoThuTu(ten):
    t=['luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi']
    for i in range(len(t)):
        if t[i]==ten:
            return i;
    return -1;


def veDacTrung2D(mangCacDacTrung,mangCacDacTrungVe,soLuongDiemVe,n_clusters):
    data=lay_data()
    #kiem tra dieu kien
    if soLuongDiemVe is not None :
        if soLuongDiemVe > len(data):
            return None
    if len(mangCacDacTrungVe)!=2:
        return None
    m=[]
    for i in mangCacDacTrungVe:
        if traSoThuTu(i)!=-1:
            m.append(traSoThuTu(i))
    mangVe=[]
    # xac dinh dac trung ve va dac trung tinh toan
    if mangCacDacTrung is None:
        kmeans=KMean(mangCacDacTrungVe,n_clusters)
    else:
        kmeans=KMean(mangCacDacTrung,n_clusters)
    # <--     -->
    #tien hanh ve
    if soLuongDiemVe is None:
        for i in range(len(data)):
            mangVe.append([data[i][m[0]],data[i][m[1]],kmeans.labels_[i]])
    else:
        for i in range(soLuongDiemVe):
            mangVe.append([data[i][m[0]],data[i][m[1]],kmeans.labels_[i]])
    centroids=kmeans.cluster_centers_
    mangVe=np.array(mangVe)
    centroids=np.array(centroids)
    plt.scatter(mangVe[:,0],mangVe[:,1],c=mangVe[:,2])
    plt.scatter(centroids[:,0],centroids[:,1],alpha=0.5,marker=r'$\clubsuit$',c='g',s=200,label="centroid")
    plt.xlabel(mangCacDacTrungVe[0])
    plt.ylabel(mangCacDacTrungVe[1])
    plt.title("Biểu đồ 2d phân cụm cho Kmeans ứng với %s cụm" %n_clusters)
    plt.legend(loc='upper left')
    plt.show()

def veDacTrung3D(mangCacDacTrung,mangCacDacTrungVe,soLuongDiemVe,n_clusters):
    data=lay_data()
    #kiem tra dieu kien
    if soLuongDiemVe is not None :
        if soLuongDiemVe > len(data):
            return None
    if len(mangCacDacTrungVe)!=3:
        return None
    m=[]
    for i in mangCacDacTrungVe:
        if traSoThuTu(i)!=-1:
            m.append(traSoThuTu(i))
    mangVe=[]
    # xac dinh dac trung ve va dac trung tinh toan
    if mangCacDacTrung is None:
        kmeans=KMean(mangCacDacTrungVe,n_clusters)
    else:
        kmeans=KMean(mangCacDacTrung,n_clusters)
    # <--     -->

    #tien hanh ve
    if soLuongDiemVe is None:
        for i in range(len(data)):
            mangVe.append([data[i][m[0]],data[i][m[1]],data[i][m[2]],kmeans.labels_[i]])
    else:
        for i in range(soLuongDiemVe):
            mangVe.append([data[i][m[0]],data[i][m[1]],data[i][m[2]],kmeans.labels_[i]])
    centroids=kmeans.cluster_centers_
    mangVe=np.array(mangVe)
    centroids=np.array(centroids)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mangVe[:,0], mangVe[:,1], mangVe[:,2], marker='o',c=mangVe[:,3])
    ax.scatter(centroids[:,0],centroids[:,1],centroids[:,2],alpha=0.5,marker=r'$\clubsuit$',c='g',s=200,label="centroid")
    ax.set_xlabel(mangCacDacTrungVe[0])
    ax.set_ylabel(mangCacDacTrungVe[1])
    ax.set_zlabel(mangCacDacTrungVe[2])
    plt.title("Biểu đồ 3d phân cụm cho Kmeans ứng với %s cụm" %n_clusters)
    ax.legend(loc='lower left')
    plt.show()

def help():
    print("\nhelp:\t\t.veTimSoCluster(mangCacDacTrung,diemBatDau,diemKetThuc)\n")
    print("\t\t.KMean(mangCacDacTrung,n_clusters) \n")
    print("\t\t.veDacTrung2D(mangCacDacTrung,mangCacDacTrungVe,soLuongDiemVe,so cum)\n")
    print("\t\t.veDacTrung3D(mangCacDacTrung,mangCacDacTrungVe,soLuongDiemVe,so cum)\n")
