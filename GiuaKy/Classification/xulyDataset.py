# coding=utf-8
import pandas as pd
x_training=[]
y_training=[]

DauVao=pd.read_csv('./dataset/dataset_for_classification.csv',encoding='utf-8')
tuoi=(DauVao['tuoi'].values).tolist()
nghe_nghiep=(DauVao['nghe_nghiep'].values).tolist()
hon_nhan=(DauVao['hon_nhan'].values).tolist()
hoc_van=(DauVao['hoc_van'].values).tolist()
co_the_tin_dung=(DauVao['co_the_tin_dung'].values).tolist()
co_nha_o=(DauVao['co_nha_o'].values).tolist()
vay_ca_nhan=(DauVao['vay_ca_nhan'].values).tolist()
kenh_lien_lac=(DauVao['kenh_lien_lac'].values).tolist()
thang_lien_lac=(DauVao['thang_lien_lac'].values).tolist()
ngay_lien_lac=(DauVao['ngay_lien_lac'].values).tolist()
thoi_luong_lien_lac=(DauVao['thoi_luong_lien_lac'].values).tolist()
so_luong_lien_lac=(DauVao['so_luong_lien_lac'].values).tolist()
ngay=(DauVao['ngay'].values).tolist()
so_luong_lien_lac_truoc_day=(DauVao['so_luong_lien_lac_truoc_day'].values).tolist()
ket_qua_lan_truoc=(DauVao['ket_qua_lan_truoc'].values).tolist()
ti_le_thay_doi_viec_lam=(DauVao['ti_le_thay_doi_viec_lam'].values).tolist()
CPI=(DauVao['CPI'].values).tolist()
CCI=(DauVao['CCI'].values).tolist()
lai_suat_3thang=(DauVao['lai_suat_3thang'].values).tolist()
so_luong_nhan_vien=(DauVao['so_luong_nhan_vien'].values).tolist()

y_training=(DauVao['label'].values).tolist()
