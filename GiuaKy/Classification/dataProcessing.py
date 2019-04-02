# coding=utf-8
import pandas as pd
import getData as gd
x_training=[]# tap du lieu training da duoc bien doi
y_training=[]# label cho tap du lieu x_training
traCuu=[]
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
def chuyen_dac_truong_sang_so(dac_trung_cu,mang_ganSoPhanLoai):
    a=[]
    for i in dac_trung_cu:
        for j in mang_ganSoPhanLoai:
            if i==j[0]:
                a.append([j[1]])
    return a;
# bat dau chuyen cac dac trung sang vector so
tuoi=chuyen_dac_truong_sang_so(gd.tuoi, ganSoPhanLoai(xoaTrung(gd.tuoi)))
nghe_nghiep=chuyen_dac_truong_sang_so(gd.nghe_nghiep, ganSoPhanLoai(xoaTrung(gd.nghe_nghiep)))
hon_nhan=chuyen_dac_truong_sang_so(gd.hon_nhan, ganSoPhanLoai(xoaTrung(gd.hon_nhan)))
hoc_van=chuyen_dac_truong_sang_so(gd.hoc_van, ganSoPhanLoai(xoaTrung(gd.hoc_van)))
co_the_tin_dung=chuyen_dac_truong_sang_so(gd.co_the_tin_dung, ganSoPhanLoai(xoaTrung(gd.co_the_tin_dung)))
co_nha_o=chuyen_dac_truong_sang_so(gd.co_nha_o, ganSoPhanLoai(xoaTrung(gd.co_nha_o)))
vay_ca_nhan=chuyen_dac_truong_sang_so(gd.vay_ca_nhan, ganSoPhanLoai(xoaTrung(gd.vay_ca_nhan)))
kenh_lien_lac=chuyen_dac_truong_sang_so(gd.kenh_lien_lac, ganSoPhanLoai(xoaTrung(gd.kenh_lien_lac)))
thang_lien_lac=chuyen_dac_truong_sang_so(gd.thang_lien_lac, ganSoPhanLoai(xoaTrung(gd.thang_lien_lac)))
ngay_lien_lac=chuyen_dac_truong_sang_so(gd.ngay_lien_lac, ganSoPhanLoai(xoaTrung(gd.ngay_lien_lac)))
thoi_luong_lien_lac=chuyen_dac_truong_sang_so(gd.thoi_luong_lien_lac, ganSoPhanLoai(xoaTrung(gd.thoi_luong_lien_lac)))
so_luong_lien_lac=chuyen_dac_truong_sang_so(gd.so_luong_lien_lac, ganSoPhanLoai(xoaTrung(gd.so_luong_lien_lac)))
ngay=chuyen_dac_truong_sang_so(gd.ngay, ganSoPhanLoai(xoaTrung(gd.ngay)))
so_luong_lien_lac_truoc_day=chuyen_dac_truong_sang_so(gd.so_luong_lien_lac_truoc_day, ganSoPhanLoai(xoaTrung(gd.so_luong_lien_lac_truoc_day)))
ket_qua_lan_truoc=chuyen_dac_truong_sang_so(gd.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(gd.ket_qua_lan_truoc)))
ti_le_thay_doi_viec_lam=chuyen_dac_truong_sang_so(gd.ti_le_thay_doi_viec_lam, ganSoPhanLoai(xoaTrung(gd.ti_le_thay_doi_viec_lam)))
CPI=chuyen_dac_truong_sang_so(gd.CPI, ganSoPhanLoai(xoaTrung(gd.CPI)))
CCI=chuyen_dac_truong_sang_so(gd.CCI, ganSoPhanLoai(xoaTrung(gd.CCI)))
lai_suat_3thang=chuyen_dac_truong_sang_so(gd.lai_suat_3thang, ganSoPhanLoai(xoaTrung(gd.lai_suat_3thang)))
so_luong_nhan_vien=chuyen_dac_truong_sang_so(gd.so_luong_nhan_vien, ganSoPhanLoai(xoaTrung(gd.so_luong_nhan_vien)))

# tao tap  du lieu x_training
for i in range(len(tuoi)):
    x_training.append([
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
# tao tap du lieu y_training
y_training=gd.label
# tao bien tra cuu thong tin
traCuu.append(['tuoi:0'])
traCuu.append(['nghe_nghiep:1'])
traCuu.append(['hon_nhan:2'])
traCuu.append(['hoc_van:3'])
traCuu.append(['co_the_tin_dung:4'])
traCuu.append(['co_nha_o:5'])
traCuu.append(['vay_ca_nhan:6'])
traCuu.append(['kenh_lien_lac:7'])
traCuu.append(['thang_lien_lac:8'])
traCuu.append(['ngay_lien_lac:9'])
traCuu.append(['thoi_luong_lien_lac:10'])
traCuu.append(['so_luong_lien_lac:11'])
traCuu.append(['ngay:12'])
traCuu.append(['so_luong_lien_lac_truoc_day:13'])
traCuu.append(['ket_qua_lan_truoc:14'])
traCuu.append(['ti_le_thay_doi_viec_lam:15'])
traCuu.append(['CPI:16'])
traCuu.append(['CCI:17'])
traCuu.append(['lai_suat_3thang:18'])
traCuu.append(['so_luong_nhan_vien:19'])



#kiem thu
#print(x_training[0])
#print(traCuu)
#print(y_training)
