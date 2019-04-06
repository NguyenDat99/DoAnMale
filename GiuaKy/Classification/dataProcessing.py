# coding=utf-8
import pandas as pd
import DataAdapter as da

dataset=da.dataset()
class traCuu:
    def __init__(seft):
        seft.tuoi='tuoi -> 0'
        seft.nghe_nghiep='nghe_nghiep -> 1'
        seft.hon_nhan='hon_nhan -> 2'
        seft.hoc_van='hoc_van -> 3'
        seft.co_the_tin_dung='co_the_tin_dung -> 4'
        seft.co_nha_o='co_nha_o -> 5'
        seft.vay_ca_nhan='vay_ca_nhan -> 6'
        seft.kenh_lien_lac='kenh_lien_lac -> 7'
        seft.thang_lien_lac='thang_lien_lac -> 8'
        seft.ngay_lien_lac='ngay_lien_lac -> 9'
        seft.thoi_luong_lien_lac='thoi_luong_lien_lac -> 10'
        seft.so_luong_lien_lac='so_luong_lien_lac -> 11'
        seft.ngay='ngay -> 12'
        seft.so_luong_lien_lac_truoc_day='so_luong_lien_lac_truoc_day -> 13'
        seft.ket_qua_lan_truoc='ket_qua_lan_truoc -> 14'
        seft.ti_le_thay_doi_viec_lam='ti_le_thay_doi_viec_lam -> 15'
        seft.CPI='CPI -> 16'
        seft.CCI='CCI -> 17'
        seft.lai_suat_3thang='lai_suat_3thang -> 18'
        seft.so_luong_nhan_vien='so_luong_nhan_vien -> 19'

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


# bat dau chuyen cac dac trung sang  so khong cho phep null
def data_khongLoc(k):
    tuoi=chuyen_dac_truong_sang_so(dataset.tuoi, ganSoPhanLoai(xoaTrung(dataset.tuoi)),0)
    nghe_nghiep=chuyen_dac_truong_sang_so(dataset.nghe_nghiep, ganSoPhanLoai(xoaTrung(dataset.nghe_nghiep)),0)
    hon_nhan=chuyen_dac_truong_sang_so(dataset.hon_nhan, ganSoPhanLoai(xoaTrung(dataset.hon_nhan)),0)
    hoc_van=chuyen_dac_truong_sang_so(dataset.hoc_van, ganSoPhanLoai(xoaTrung(dataset.hoc_van)),0)
    co_the_tin_dung=chuyen_dac_truong_sang_so(dataset.co_the_tin_dung, ganSoPhanLoai(xoaTrung(dataset.co_the_tin_dung)),0)
    co_nha_o=chuyen_dac_truong_sang_so(dataset.co_nha_o, ganSoPhanLoai(xoaTrung(dataset.co_nha_o)),0)
    vay_ca_nhan=chuyen_dac_truong_sang_so(dataset.vay_ca_nhan, ganSoPhanLoai(xoaTrung(dataset.vay_ca_nhan)),0)
    kenh_lien_lac=chuyen_dac_truong_sang_so(dataset.kenh_lien_lac, ganSoPhanLoai(xoaTrung(dataset.kenh_lien_lac)),0)
    thang_lien_lac=chuyen_dac_truong_sang_so(dataset.thang_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thang_lien_lac)),0)
    ngay_lien_lac=chuyen_dac_truong_sang_so(dataset.ngay_lien_lac, ganSoPhanLoai(xoaTrung(dataset.ngay_lien_lac)),0)
    thoi_luong_lien_lac=chuyen_dac_truong_sang_so(dataset.thoi_luong_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thoi_luong_lien_lac)),0)
    so_luong_lien_lac=chuyen_dac_truong_sang_so(dataset.so_luong_lien_lac, ganSoPhanLoai(xoaTrung(dataset.so_luong_lien_lac)),0)
    ngay=chuyen_dac_truong_sang_so(dataset.ngay, ganSoPhanLoai(xoaTrung(dataset.ngay)),0)
    so_luong_lien_lac_truoc_day=chuyen_dac_truong_sang_so(dataset.so_luong_lien_lac_truoc_day, ganSoPhanLoai(xoaTrung(dataset.so_luong_lien_lac_truoc_day)),0)
    ket_qua_lan_truoc=chuyen_dac_truong_sang_so(dataset.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(dataset.ket_qua_lan_truoc)),0)
    ti_le_thay_doi_viec_lam=chuyen_dac_truong_sang_so(dataset.ti_le_thay_doi_viec_lam, ganSoPhanLoai(xoaTrung(dataset.ti_le_thay_doi_viec_lam)),0)
    CPI=chuyen_dac_truong_sang_so(dataset.CPI, ganSoPhanLoai(xoaTrung(dataset.CPI)),0)
    CCI=chuyen_dac_truong_sang_so(dataset.CCI, ganSoPhanLoai(xoaTrung(dataset.CCI)),0)
    lai_suat_3thang=chuyen_dac_truong_sang_so(dataset.lai_suat_3thang, ganSoPhanLoai(xoaTrung(dataset.lai_suat_3thang)),0)
    so_luong_nhan_vien=chuyen_dac_truong_sang_so(dataset.so_luong_nhan_vien, ganSoPhanLoai(xoaTrung(dataset.so_luong_nhan_vien)),0)

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
    if(k==0):
        return x_training_khongLoc
    elif k==1:
        return da.dataset().label

# bat dau chuyen cac dac trung sang vector so cho phep null
tuoi1=chuyen_dac_truong_sang_so(dataset.tuoi, ganSoPhanLoai(xoaTrung(dataset.tuoi)),1)
nghe_nghiep1=chuyen_dac_truong_sang_so(dataset.nghe_nghiep, ganSoPhanLoai(xoaTrung(dataset.nghe_nghiep)),1)
hon_nhan1=chuyen_dac_truong_sang_so(dataset.hon_nhan, ganSoPhanLoai(xoaTrung(dataset.hon_nhan)),1)
hoc_van1=chuyen_dac_truong_sang_so(dataset.hoc_van, ganSoPhanLoai(xoaTrung(dataset.hoc_van)),1)
co_the_tin_dung1=chuyen_dac_truong_sang_so(dataset.co_the_tin_dung, ganSoPhanLoai(xoaTrung(dataset.co_the_tin_dung)),1)
co_nha_o1=chuyen_dac_truong_sang_so(dataset.co_nha_o, ganSoPhanLoai(xoaTrung(dataset.co_nha_o)),1)
vay_ca_nhan1=chuyen_dac_truong_sang_so(dataset.vay_ca_nhan, ganSoPhanLoai(xoaTrung(dataset.vay_ca_nhan)),1)
kenh_lien_lac1=chuyen_dac_truong_sang_so(dataset.kenh_lien_lac, ganSoPhanLoai(xoaTrung(dataset.kenh_lien_lac)),1)
thang_lien_lac1=chuyen_dac_truong_sang_so(dataset.thang_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thang_lien_lac)),1)
ngay_lien_lac1=chuyen_dac_truong_sang_so(dataset.ngay_lien_lac, ganSoPhanLoai(xoaTrung(dataset.ngay_lien_lac)),1)
thoi_luong_lien_lac1=chuyen_dac_truong_sang_so(dataset.thoi_luong_lien_lac, ganSoPhanLoai(xoaTrung(dataset.thoi_luong_lien_lac)),1)
so_luong_lien_lac1=chuyen_dac_truong_sang_so(dataset.so_luong_lien_lac, ganSoPhanLoai(xoaTrung(dataset.so_luong_lien_lac)),1)
ngay1=chuyen_dac_truong_sang_so(dataset.ngay, ganSoPhanLoai(xoaTrung(dataset.ngay)),1)
so_luong_lien_lac_truoc_day1=chuyen_dac_truong_sang_so(dataset.so_luong_lien_lac_truoc_day, ganSoPhanLoai(xoaTrung(dataset.so_luong_lien_lac_truoc_day)),1)
ket_qua_lan_truoc1=chuyen_dac_truong_sang_so(dataset.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(dataset.ket_qua_lan_truoc)),1)
ti_le_thay_doi_viec_lam1=chuyen_dac_truong_sang_so(dataset.ti_le_thay_doi_viec_lam, ganSoPhanLoai(xoaTrung(dataset.ti_le_thay_doi_viec_lam)),1)
CPI1=chuyen_dac_truong_sang_so(dataset.CPI, ganSoPhanLoai(xoaTrung(dataset.CPI)),1)
CCI1=chuyen_dac_truong_sang_so(dataset.CCI, ganSoPhanLoai(xoaTrung(dataset.CCI)),1)
lai_suat_3thang1=chuyen_dac_truong_sang_so(dataset.lai_suat_3thang, ganSoPhanLoai(xoaTrung(dataset.lai_suat_3thang)),1)
so_luong_nhan_vien1=chuyen_dac_truong_sang_so(dataset.so_luong_nhan_vien, ganSoPhanLoai(xoaTrung(dataset.so_luong_nhan_vien)),1)
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
def data_CoLoc(k):
    if k==0:
        return x_training_CoLoc
    elif k==1:
        return y_training_CL
print("\t\t\t 3 -> Xử lý dữ liệu thành công!")
