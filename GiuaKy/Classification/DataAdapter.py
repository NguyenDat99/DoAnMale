# coding=utf-8
import pandas as pd
DauVao=pd.read_csv('./dataset/dataset_for_classification.csv',encoding='utf-8')
# lay dataset tu file  len va cung cap method lay tung cot tuong ung cua dataset do
def getFeature(name):

    if name=='thoi_luong_lien_lac':
        o=[]
        for i in DauVao[name].values:
            o.append(int((i*13.999-13)/999))
    else:
            o=(DauVao[name].values).tolist()
    return  o

class dataset:
    def __init__(seft):
        seft.tuoi=getFeature('tuoi')
        seft.nghe_nghiep=getFeature('nghe_nghiep')
        seft.hon_nhan=getFeature('hon_nhan')
        seft.hoc_van=getFeature('hoc_van')
        seft.co_the_tin_dung=getFeature('co_the_tin_dung')
        seft.co_nha_o=getFeature('co_nha_o')
        seft.vay_ca_nhan=getFeature('vay_ca_nhan')
        seft.kenh_lien_lac=getFeature('kenh_lien_lac')
        seft.thang_lien_lac=getFeature('thang_lien_lac')
        seft.ngay_lien_lac=getFeature('ngay_lien_lac')
        seft.thoi_luong_lien_lac= getFeature('thoi_luong_lien_lac')
        seft.so_luong_lien_lac=getFeature('so_luong_lien_lac')
        seft.ngay=getFeature('ngay')
        seft.so_luong_lien_lac_truoc_day=getFeature('so_luong_lien_lac_truoc_day')
        seft.ket_qua_lan_truoc=getFeature('ket_qua_lan_truoc')
        seft.ti_le_thay_doi_viec_lam=getFeature('ti_le_thay_doi_viec_lam')
        seft.CPI=getFeature('CPI')
        seft.CCI=getFeature('CCI')
        seft.lai_suat_3thang=getFeature('lai_suat_3thang')
        seft.so_luong_nhan_vien=getFeature('so_luong_nhan_vien')
        seft.label=getFeature('label')

print("\t\t\t 1 -> Kết nối dữ liệu thành công!")
