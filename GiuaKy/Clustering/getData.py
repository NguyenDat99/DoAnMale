# coding=utf-8
import pandas as pd
DauVao=pd.read_csv('./dataset/dataset_for_clustering.csv',encoding='utf-8')


ten_xe=(DauVao['ten_xe'].values).tolist()
luong_hao_xang=(DauVao['luong_hao_xang'].values).tolist()
so_luong_xi_lanh=(DauVao['so_luong_xi_lanh'].values).tolist()
the_tich_dong_co=(DauVao['the_tich_dong_co'].values).tolist()
ma_luc=(DauVao['ma_luc'].values).tolist()
ty_le_truc_sau=(DauVao['ty_le_truc_sau'].values).tolist()
khoi_luong_xe=(DauVao['khoi_luong_xe'].values).tolist()
gia_toc_xe=(DauVao['gia_toc_xe'].values).tolist()
loai_xy_lanh_dong_co=(DauVao['loai_xy_lanh_dong_co'].values).tolist()
loai_truyen_dong=(DauVao['loai_truyen_dong'].values).tolist()
so_luong_banh_rang=(DauVao['so_luong_banh_rang'].values).tolist()
so_luong_bo_che_hoa_khi=(DauVao['so_luong_bo_che_hoa_khi'].values).tolist()
