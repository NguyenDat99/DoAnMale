# coding=utf-8
import sys
sys.path.append('../DTO/')
import pandas as pd
import DataAdapter as da
from multiprocessing.dummy import Pool as ThreadPool



dataset=da.dataset()
# xoa phan tu trung lap va cho gia tri unknown anh xa --> 0
def xoaTrung(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    for i in range(len(b)):
        if b[i]=='unknown':
            b[0],b[i]=b[i],b[0]
    return b
# ham chuyen doi qua so cho cac gia tri da xoa trung
def ganSoPhanLoai(mangXoaTrung):
    b=[]
    for i in range(len(mangXoaTrung)):
        b.append([mangXoaTrung[i],i])
    return b
# ham chuyen cac dac trung ban dau thanh dang so
def chuyen_dac_truong_sang_so(dac_trung_cu,mang_ganSoPhanLoai,f):
    a=[]
    for i in dac_trung_cu:
        if f==0:
            for j in mang_ganSoPhanLoai:
                if i==j[0]:
                    a.append(j[1])
# ham chuyen cac dac trung ban dau thanh dang so neu gia tri unknown thi chuyen thanh null
        elif f==1:
            for j in mang_ganSoPhanLoai:
                if i==j[0] and i!= 'unknown':
                    a.append(j[1])
                elif  i== 'unknown' and i==j[0]:
                    a.append(None)
    return a;
def traSoThuTu(ten):
    t=['tuoi','nghe_nghiep','hon_nhan','hoc_van','co_the_tin_dung',
    'co_nha_o','vay_ca_nhan','kenh_lien_lac','thang_lien_lac',
    'ngay_lien_lac','thoi_luong_lien_lac','so_luong_lien_lac',
    'ngay','so_luong_lien_lac_truoc_day','ket_qua_lan_truoc',
    'ti_le_thay_doi_viec_lam','CPI','CCI','lai_suat_3thang',
    'so_luong_nhan_vien']
    for i in range(len(t)):
        if t[i]==ten:
            return i;
    return -1;
# bat dau chuyen cac dac trung sang  so khong cho phep null
def data_khongLoc(_k,array):
    k=[]
    data=[]
    nghe_nghiep=chuyen_dac_truong_sang_so(dataset.nghe_nghiep, ganSoPhanLoai(xoaTrung(dataset.nghe_nghiep)),0)
    hon_nhan=chuyen_dac_truong_sang_so(dataset.hon_nhan, ganSoPhanLoai(xoaTrung(dataset.hon_nhan)),0)
    hoc_van=chuyen_dac_truong_sang_so(dataset.hoc_van, ganSoPhanLoai(xoaTrung(dataset.hoc_van)),0)
    co_the_tin_dung=chuyen_dac_truong_sang_so(dataset.co_the_tin_dung, ganSoPhanLoai(xoaTrung(dataset.co_the_tin_dung)),0)
    co_nha_o=chuyen_dac_truong_sang_so(dataset.co_nha_o, ganSoPhanLoai(xoaTrung(dataset.co_nha_o)),0)
    vay_ca_nhan=chuyen_dac_truong_sang_so(dataset.vay_ca_nhan, ganSoPhanLoai(xoaTrung(dataset.vay_ca_nhan)),0)
    kenh_lien_lac=chuyen_dac_truong_sang_so(dataset.kenh_lien_lac, ganSoPhanLoai(xoaTrung(dataset.kenh_lien_lac)),0)
    thang_lien_lac=chuyen_dac_truong_sang_so(dataset.thang_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thang_lien_lac)),0)
    ngay_lien_lac=chuyen_dac_truong_sang_so(dataset.ngay_lien_lac, ganSoPhanLoai(xoaTrung(dataset.ngay_lien_lac)),0)
    ngay=chuyen_dac_truong_sang_so(dataset.ngay, ganSoPhanLoai(xoaTrung(dataset.ngay)),0)
    ket_qua_lan_truoc=chuyen_dac_truong_sang_so(dataset.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(dataset.ket_qua_lan_truoc)),0)
    tuoi=dataset.tuoi
    thoi_luong_lien_lac=dataset.thoi_luong_lien_lac
    so_luong_lien_lac=dataset.so_luong_lien_lac
    so_luong_lien_lac_truoc_day=dataset.so_luong_lien_lac_truoc_day
    ti_le_thay_doi_viec_lam=dataset.ti_le_thay_doi_viec_lam
    CPI=dataset.CPI
    CCI=dataset.CCI
    lai_suat_3thang=dataset.lai_suat_3thang
    so_luong_nhan_vien=dataset.so_luong_nhan_vien

    x_training_khongLoc=[]
    # tao tap  du lieu x_training khong loc unknown
    for i in range(len(tuoi)):
        x_training_khongLoc.append([
            tuoi[i]
            ,nghe_nghiep[i]
            ,hon_nhan[i]
            ,hoc_van[i]
            ,co_the_tin_dung[i]
            ,co_nha_o[i]
            ,vay_ca_nhan[i]
            ,kenh_lien_lac[i]
            ,thang_lien_lac[i]
            ,ngay_lien_lac[i]
            ,thoi_luong_lien_lac[i]
            ,so_luong_lien_lac[i]
            ,ngay[i]
            ,so_luong_lien_lac_truoc_day[i]
            ,ket_qua_lan_truoc[i]
            ,ti_le_thay_doi_viec_lam[i]
            ,CPI[i]
            ,CCI[i]
            ,lai_suat_3thang[i]
            ,so_luong_nhan_vien[i]
            ])
    if _k==0 and array is None:
        return x_training_khongLoc
    elif _k==1 and array is None:
        return da.dataset().label
    elif array is not  None:
        if len(array)>19:
            return None;
        else:
            for i in array:
                if traSoThuTu(i)!=-1:
                    k.append(traSoThuTu(i))
            for i in range(len(x_training_khongLoc)):
                k1=[]
                for j in k:
                    k1.append(x_training_khongLoc[i][j])
                data.append(k1)
            return data;

# bat dau chuyen cac dac trung sang vector so cho phep null
nghe_nghiep1=chuyen_dac_truong_sang_so(dataset.nghe_nghiep, ganSoPhanLoai(xoaTrung(dataset.nghe_nghiep)),1)
hon_nhan1=chuyen_dac_truong_sang_so(dataset.hon_nhan, ganSoPhanLoai(xoaTrung(dataset.hon_nhan)),1)
hoc_van1=chuyen_dac_truong_sang_so(dataset.hoc_van, ganSoPhanLoai(xoaTrung(dataset.hoc_van)),1)
co_the_tin_dung1=chuyen_dac_truong_sang_so(dataset.co_the_tin_dung, ganSoPhanLoai(xoaTrung(dataset.co_the_tin_dung)),1)
co_nha_o1=chuyen_dac_truong_sang_so(dataset.co_nha_o, ganSoPhanLoai(xoaTrung(dataset.co_nha_o)),1)
vay_ca_nhan1=chuyen_dac_truong_sang_so(dataset.vay_ca_nhan, ganSoPhanLoai(xoaTrung(dataset.vay_ca_nhan)),1)
kenh_lien_lac1=chuyen_dac_truong_sang_so(dataset.kenh_lien_lac, ganSoPhanLoai(xoaTrung(dataset.kenh_lien_lac)),1)
thang_lien_lac1=chuyen_dac_truong_sang_so(dataset.thang_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thang_lien_lac)),1)
ngay_lien_lac1=chuyen_dac_truong_sang_so(dataset.ngay_lien_lac, ganSoPhanLoai(xoaTrung(dataset.ngay_lien_lac)),1)
ngay1=chuyen_dac_truong_sang_so(dataset.ngay, ganSoPhanLoai(xoaTrung(dataset.ngay)),1)
ket_qua_lan_truoc1=chuyen_dac_truong_sang_so(dataset.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(dataset.ket_qua_lan_truoc)),1)
tuoi1=dataset.tuoi
thoi_luong_lien_lac1=dataset.thoi_luong_lien_lac
so_luong_lien_lac1=dataset.so_luong_lien_lac
so_luong_lien_lac_truoc_day1=dataset.so_luong_lien_lac_truoc_day
ti_le_thay_doi_viec_lam1=dataset.ti_le_thay_doi_viec_lam
CPI1=dataset.CPI
CCI1=dataset.CCI
lai_suat_3thang1=dataset.lai_suat_3thang
so_luong_nhan_vien1=dataset.so_luong_nhan_vien
# tao tap  du lieu x_training co loc du lieu unknown
x_training_CoLoc=[]
for i in range(len(tuoi1)):
            x_training_CoLoc.append([
            tuoi1[i]
            ,nghe_nghiep1[i]
            ,hon_nhan1[i]
            ,hoc_van1[i]
            ,co_the_tin_dung1[i]
            ,co_nha_o1[i]
            ,vay_ca_nhan1[i]
            ,kenh_lien_lac1[i]
            ,thang_lien_lac1[i]
            ,ngay_lien_lac1[i]
            ,thoi_luong_lien_lac1[i]
            ,so_luong_lien_lac1[i]
            ,ngay1[i]
            ,so_luong_lien_lac_truoc_day1[i]
            ,ket_qua_lan_truoc1[i]
            ,ti_le_thay_doi_viec_lam1[i]
            ,CPI1[i]
            ,CCI1[i]
            ,lai_suat_3thang1[i]
            ,so_luong_nhan_vien1[i]
            ])
# bat dau loc du lieu x_training_coLoc chua unknown
y_training_CL=da.dataset().label
i=len(x_training_CoLoc)-1
while i>=0:
    if i<len(x_training_CoLoc) :
        for j in x_training_CoLoc[i]:
            if j is None:
                x_training_CoLoc.pop(i)
                y_training_CL.pop(i)
                break
    i-=1
def data_CoLoc(_k,array):
    k=[]
    data=[]
    if _k==0 and array is None:
        return x_training_CoLoc
    elif _k==1 and array is None:
        return y_training_CL
    elif array is not  None:
        if len(array)>19:
            return None;
        else:
            for i in array:
                if traSoThuTu(i)!=-1:
                    k.append(traSoThuTu(i))
            for i in range(len(x_training_CoLoc)):
                k1=[]
                for j in k:
                    k1.append(x_training_CoLoc[i][j])
                data.append(k1)
            return data;
#print("\t\t\t 2 -> Xử lý dữ liệu thành công!")



#cu phap coi day nhe
# print(data_khongLoc(0,None)[2])
# print(data_khongLoc(0,['tuoi','nghe_nghiep','hon_nhan','kenh_lien_lac','so_luong_nhan_vien'])[2])
# print("___")
# print(data_CoLoc(0,None)[0])
# print(data_CoLoc(0,['tuoi','nghe_nghiep','hon_nhan','kenh_lien_lac','so_luong_nhan_vien'])[0])
