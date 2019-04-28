
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import dataProcessing as dp
from scipy.cluster.hierarchy import dendrogram, linkage

def lay_data():
    data=dp.dataset(['luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi'])
    return data

def HC(mangCacDacTrung,n_clusters):
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
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward').fit(data)
    return hc

def vitriCat(n_clusters):
    switcher = {
        2: 100,
        3: 62,
        4:50,
        5:40,
        6:30,
        7:27,
        8:24
    }
    return switcher.get(n_clusters, 0)

def ve_HC(mangCacDacTrung,n_clusters):
    data = HC(mangCacDacTrung,n_clusters).children_
    Z = linkage(data)
    dendrogram(Z=Z)
    if mangCacDacTrung is None:
        y=vitriCat(n_clusters)
        plt.axhline(y=y,c="black")
    plt.show()


def help():
    print("\nhelp:\t\t.HC(mangCacDacTrung,n_clusters) tra ve HC\n")
    print("\t\t.ve_HC(mangCacDacTrung,n_clusters)\n")
