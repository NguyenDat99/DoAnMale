import dataProcessing as dp
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
data=dp.dataset(['luong_hao_xang',
'so_luong_xi_lanh','the_tich_dong_co',
'ma_luc','ty_le_truc_sau','khoi_luong_xe',
'gia_toc_xe','loai_xy_lanh_dong_co',
'loai_truyen_dong','so_luong_banh_rang',
'so_luong_bo_che_hoa_khi'])


class bestParams:
    def __init__(seft,cluster):
        seft.cluster=cluster
cluster=[]
for i in range(1,30):
        kmeans = KMeans(n_clusters=i, random_state=0).fit(data)
        cluster.append([i,kmeans.inertia_])

cluster=np.array(cluster)
plt.scatter(cluster[:,0],cluster[:,1])
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

def veDacTrung(mangCacDacTrungVe,soLuongDiemVe):
    if soLuongDiemVe is not None :
        if soLuongDiemVe > len(data):
            return None
    if len(mangCacDacTrungVe)>2:
        return None
    m=[]
    for i in mangCacDacTrungVe:
        if traSoThuTu(i)!=-1:
            m.append(traSoThuTu(i))
    mangVe=[]
    if soLuongDiemVe is None:
        for i in range(len(data)):
            mangVe.append([data[i][m[0]],data[i][m[1]],kmeans.labels_[i]])
    else:
        for i in range(soLuongDiemVe):
            mangVe.append([data[i][m[0]],data[i][m[1]],kmeans.labels_[i]])
    mangVe=np.array(mangVe)
    plt.scatter(mangVe[:,0],mangVe[:,1],c=mangVe[:,2],label=mangVe[:,2])
    plt.show()
