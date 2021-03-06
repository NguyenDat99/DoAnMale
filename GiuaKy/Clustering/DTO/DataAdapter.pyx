# coding=utf-8
import pandas as pd
import datetime
from multiprocessing.dummy import Pool as ThreadPool
DauVao=pd.read_csv('../DTO/dataset/dataset_for_clustering.csv',encoding='utf-8')

def getFeature(name):
    return  (DauVao[name].values).tolist()

def multiprocessing():
    t=['ten_xe','luong_hao_xang','so_luong_xi_lanh',
    'the_tich_dong_co','ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi']
    pool = ThreadPool(4)
    data=pool.map(getFeature,t)
    return data

class dataset:
    def __init__(seft):
        data=multiprocessing()
        seft.ten_xe=data[0]
        seft.luong_hao_xang=data[1]
        seft.so_luong_xi_lanh=data[2]
        seft.the_tich_dong_co=data[3]
        seft.ma_luc=data[4]
        seft.ty_le_truc_sau=data[5]
        seft.khoi_luong_xe=data[6]
        seft.gia_toc_xe=data[7]
        seft.loai_xy_lanh_dong_co=data[8]
        seft.loai_truyen_dong=data[9]
        seft.so_luong_banh_rang=data[10]
        seft.so_luong_bo_che_hoa_khi=data[11]
def xuatFile(KMeans_labels_,HC_labels_):
    data=dataset()
    df = pd.DataFrame({
    'ten_xe': data.ten_xe,
    'luong_hao_xang': data.luong_hao_xang,
    'so_luong_xi_lanh':data.so_luong_xi_lanh,
    'the_tich_dong_co':data.the_tich_dong_co,
    'ma_luc':data.ma_luc,
    'ty_le_truc_sau':data.ty_le_truc_sau,
    'khoi_luong_xe':data.khoi_luong_xe,
    'gia_toc_xe':data.gia_toc_xe,
    'loai_xy_lanh_dong_co':data.loai_xy_lanh_dong_co,
    'loai_truyen_dong':data.loai_truyen_dong,
    'so_luong_banh_rang':data.so_luong_banh_rang,
    'so_luong_bo_che_hoa_khi':data.so_luong_bo_che_hoa_khi,
    'KMeans_labels_':KMeans_labels_,
    'HC_labels_':HC_labels_
    })
    df.to_csv('../DTO/dataset/ketqua.csv',encoding='utf-8',index=False)
    print("\t\t\t   -> Xuất dữ liệu thành công!")
