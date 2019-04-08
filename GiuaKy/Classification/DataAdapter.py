# coding=utf-8
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
DauVao=pd.read_csv('./dataset/dataset_for_classification.csv',encoding='utf-8')
# lay dataset tu file  len va cung cap method lay tung cot tuong ung cua dataset do
def getFeature(name):

    if name=='thoi_luong_lien_lac' or name=='so_luong_nhan_vien':
        o=[]
        for i in DauVao[name].values:
            o.append(int((i*13.999-13)/999))
    else:
            o=(DauVao[name].values).tolist()
    return  o
def multiprocessing():
    t=['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
    'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
    'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
    'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
    'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
    'so_luong_nhan_vien','label']
    pool = ThreadPool(4)
    data=pool.map(getFeature,t)
    return data
class dataset:
    def __init__(seft):
        data=multiprocessing()
        seft.tuoi=data[0]
        seft.nghe_nghiep=data[1]
        seft.hon_nhan=data[2]
        seft.hoc_van=data[3]
        seft.co_the_tin_dung=data[4]
        seft.co_nha_o=data[5]
        seft.vay_ca_nhan=data[6]
        seft.kenh_lien_lac=data[7]
        seft.thang_lien_lac=data[8]
        seft.ngay_lien_lac=data[9]
        seft.thoi_luong_lien_lac= data[10]
        seft.so_luong_lien_lac=data[11]
        seft.ngay=data[12]
        seft.so_luong_lien_lac_truoc_day=data[13]
        seft.ket_qua_lan_truoc=data[14]
        seft.ti_le_thay_doi_viec_lam=data[15]
        seft.CPI=data[16]
        seft.CCI=data[17]
        seft.lai_suat_3thang=data[18]
        seft.so_luong_nhan_vien=data[19]
        seft.label=data[20]

print("\t\t\t 1 -> Kết nối dữ liệu thành công!")
