import sys
sys.path.append('../BUS/')
import KMeans
import Hc
import dataProcessing as dp
            # KMeans
def KM():
    #KMeans.help()
    KMeans.veTimSoCluster(['luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi'],1,7)

    km=KMeans.KMean(['luong_hao_xang',
    'so_luong_xi_lanh','the_tich_dong_co',
    'ma_luc','ty_le_truc_sau','khoi_luong_xe',
    'gia_toc_xe','loai_xy_lanh_dong_co',
    'loai_truyen_dong','so_luong_banh_rang',
    'so_luong_bo_che_hoa_khi'],2)

    KMeans.veDacTrung2D(['gia_toc_xe','the_tich_dong_co'
    ],['gia_toc_xe','the_tich_dong_co'],None,2)

    KMeans.veDacTrung3D(['gia_toc_xe','khoi_luong_xe','the_tich_dong_co'
    ],['gia_toc_xe','khoi_luong_xe','the_tich_dong_co',],None,2)
    return km

            #HC
def hc():
    #Hc.help()
    Hc.ve_HC(None,2)
    hc=Hc.HC(None,2)
    return hc

            #xuatFile
def xuatFile(km,hc):
    dp.xuatFile(km,hc)


xuatFile(KM(),hc())
