import sys
sys.path.append('../DTO/')
import DataAdapter

def traSoThuTu(ten):
    t=['ten_xe','luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi']
    for i in range(len(t)):
        if t[i]==ten:
            return i;
    return -1;
def chuyenData():
    data=DataAdapter.dataset()
    ten_xe=data.ten_xe
    luong_hao_xang=data.luong_hao_xang
    so_luong_xi_lanh=data.so_luong_xi_lanh
    the_tich_dong_co=data.the_tich_dong_co
    ma_luc=data.ma_luc
    ty_le_truc_sau=data.ty_le_truc_sau
    khoi_luong_xe=data.khoi_luong_xe
    gia_toc_xe=data.gia_toc_xe
    loai_xy_lanh_dong_co=data.loai_xy_lanh_dong_co
    loai_truyen_dong=data.loai_truyen_dong
    so_luong_banh_rang=data.so_luong_banh_rang
    so_luong_bo_che_hoa_khi=data.so_luong_bo_che_hoa_khi
    dataset=[]
    for i in range(len(ten_xe)):
         dataset.append([ten_xe[i],luong_hao_xang[i],
         so_luong_xi_lanh[i],the_tich_dong_co[i],ma_luc[i],ty_le_truc_sau[i],
         khoi_luong_xe[i],gia_toc_xe[i],loai_xy_lanh_dong_co[i],
         loai_truyen_dong[i],so_luong_banh_rang[i],
         so_luong_bo_che_hoa_khi[i]])
    return dataset

def dataset(array):
    dt=chuyenData()
    if array is None:
        return dt
    else:
        k=[]
        data=[]
        for i in array :
            if traSoThuTu(i)!=-1:
                k.append(traSoThuTu(i))
        for i in range(len(dt)):
            k1=[]
            for j in k:
                k1.append(dt[i][j])
            data.append(k1)
        return data


                        #xuatFile
def xuatFile(km,hc):
    DataAdapter.xuatFile(km.labels_,hc.labels_)
