# coding=utf-8
import pandas as pd
import DataAdapter as da
x_training_khongLoc=[]# tap du lieu training da duoc bien doi khong null
x_training_coLoc=[]
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
                a.append(j[1])
    return a;
# ham chuyen cac dac trung ban dau thanh dang so neu gia tri unknown thi chuyen thanh null
def chuyen_dac_truong_sang_so_co_Null(dac_trung_cu,mang_ganSoPhanLoai):
    a=[]
    for i in dac_trung_cu:
        for j in mang_ganSoPhanLoai:
            if i==j[0] and i!= 'unknown':
                a.append(j[1])
            elif  i== 'unknown' and i==j[0]:
                a.append(None)
    return a;




# bat dau chuyen cac dac trung sang vector so khong cho phep null
tuoi=chuyen_dac_truong_sang_so(da.tuoi, ganSoPhanLoai(xoaTrung(da.tuoi)))
nghe_nghiep=chuyen_dac_truong_sang_so(da.nghe_nghiep, ganSoPhanLoai(xoaTrung(da.nghe_nghiep)))
hon_nhan=chuyen_dac_truong_sang_so(da.hon_nhan, ganSoPhanLoai(xoaTrung(da.hon_nhan)))
hoc_van=chuyen_dac_truong_sang_so(da.hoc_van, ganSoPhanLoai(xoaTrung(da.hoc_van)))
co_the_tin_dung=chuyen_dac_truong_sang_so(da.co_the_tin_dung, ganSoPhanLoai(xoaTrung(da.co_the_tin_dung)))
co_nha_o=chuyen_dac_truong_sang_so(da.co_nha_o, ganSoPhanLoai(xoaTrung(da.co_nha_o)))
vay_ca_nhan=chuyen_dac_truong_sang_so(da.vay_ca_nhan, ganSoPhanLoai(xoaTrung(da.vay_ca_nhan)))
kenh_lien_lac=chuyen_dac_truong_sang_so(da.kenh_lien_lac, ganSoPhanLoai(xoaTrung(da.kenh_lien_lac)))
thang_lien_lac=chuyen_dac_truong_sang_so(da.thang_lien_lac, ganSoPhanLoai(xoaTrung(da.thang_lien_lac)))
ngay_lien_lac=chuyen_dac_truong_sang_so(da.ngay_lien_lac, ganSoPhanLoai(xoaTrung(da.ngay_lien_lac)))
thoi_luong_lien_lac=chuyen_dac_truong_sang_so(da.thoi_luong_lien_lac, ganSoPhanLoai(xoaTrung(da.thoi_luong_lien_lac)))
so_luong_lien_lac=chuyen_dac_truong_sang_so(da.so_luong_lien_lac, ganSoPhanLoai(xoaTrung(da.so_luong_lien_lac)))
ngay=chuyen_dac_truong_sang_so(da.ngay, ganSoPhanLoai(xoaTrung(da.ngay)))
so_luong_lien_lac_truoc_day=chuyen_dac_truong_sang_so(da.so_luong_lien_lac_truoc_day, ganSoPhanLoai(xoaTrung(da.so_luong_lien_lac_truoc_day)))
ket_qua_lan_truoc=chuyen_dac_truong_sang_so(da.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(da.ket_qua_lan_truoc)))
ti_le_thay_doi_viec_lam=chuyen_dac_truong_sang_so(da.ti_le_thay_doi_viec_lam, ganSoPhanLoai(xoaTrung(da.ti_le_thay_doi_viec_lam)))
CPI=chuyen_dac_truong_sang_so(da.CPI, ganSoPhanLoai(xoaTrung(da.CPI)))
CCI=chuyen_dac_truong_sang_so(da.CCI, ganSoPhanLoai(xoaTrung(da.CCI)))
lai_suat_3thang=chuyen_dac_truong_sang_so(da.lai_suat_3thang, ganSoPhanLoai(xoaTrung(da.lai_suat_3thang)))
so_luong_nhan_vien=chuyen_dac_truong_sang_so(da.so_luong_nhan_vien, ganSoPhanLoai(xoaTrung(da.so_luong_nhan_vien)))



# bat dau chuyen cac dac trung sang vector so cho phep null
tuoi1=chuyen_dac_truong_sang_so_co_Null(da.tuoi, ganSoPhanLoai(xoaTrung(da.tuoi)))
nghe_nghiep1=chuyen_dac_truong_sang_so_co_Null(da.nghe_nghiep, ganSoPhanLoai(xoaTrung(da.nghe_nghiep)))
hon_nhan1=chuyen_dac_truong_sang_so_co_Null(da.hon_nhan, ganSoPhanLoai(xoaTrung(da.hon_nhan)))
hoc_van1=chuyen_dac_truong_sang_so_co_Null(da.hoc_van, ganSoPhanLoai(xoaTrung(da.hoc_van)))
co_the_tin_dung1=chuyen_dac_truong_sang_so_co_Null(da.co_the_tin_dung, ganSoPhanLoai(xoaTrung(da.co_the_tin_dung)))
co_nha_o1=chuyen_dac_truong_sang_so_co_Null(da.co_nha_o, ganSoPhanLoai(xoaTrung(da.co_nha_o)))
vay_ca_nhan1=chuyen_dac_truong_sang_so_co_Null(da.vay_ca_nhan, ganSoPhanLoai(xoaTrung(da.vay_ca_nhan)))
kenh_lien_lac1=chuyen_dac_truong_sang_so_co_Null(da.kenh_lien_lac, ganSoPhanLoai(xoaTrung(da.kenh_lien_lac)))
thang_lien_lac1=chuyen_dac_truong_sang_so_co_Null(da.thang_lien_lac, ganSoPhanLoai(xoaTrung(da.thang_lien_lac)))
ngay_lien_lac1=chuyen_dac_truong_sang_so_co_Null(da.ngay_lien_lac, ganSoPhanLoai(xoaTrung(da.ngay_lien_lac)))
thoi_luong_lien_lac1=chuyen_dac_truong_sang_so_co_Null(da.thoi_luong_lien_lac, ganSoPhanLoai(xoaTrung(da.thoi_luong_lien_lac)))
so_luong_lien_lac1=chuyen_dac_truong_sang_so_co_Null(da.so_luong_lien_lac, ganSoPhanLoai(xoaTrung(da.so_luong_lien_lac)))
ngay1=chuyen_dac_truong_sang_so_co_Null(da.ngay, ganSoPhanLoai(xoaTrung(da.ngay)))
so_luong_lien_lac_truoc_day1=chuyen_dac_truong_sang_so_co_Null(da.so_luong_lien_lac_truoc_day, ganSoPhanLoai(xoaTrung(da.so_luong_lien_lac_truoc_day)))
ket_qua_lan_truoc1=chuyen_dac_truong_sang_so_co_Null(da.ket_qua_lan_truoc, ganSoPhanLoai(xoaTrung(da.ket_qua_lan_truoc)))
ti_le_thay_doi_viec_lam1=chuyen_dac_truong_sang_so_co_Null(da.ti_le_thay_doi_viec_lam, ganSoPhanLoai(xoaTrung(da.ti_le_thay_doi_viec_lam)))
CPI1=chuyen_dac_truong_sang_so_co_Null(da.CPI, ganSoPhanLoai(xoaTrung(da.CPI)))
CCI1=chuyen_dac_truong_sang_so_co_Null(da.CCI, ganSoPhanLoai(xoaTrung(da.CCI)))
lai_suat_3thang1=chuyen_dac_truong_sang_so_co_Null(da.lai_suat_3thang, ganSoPhanLoai(xoaTrung(da.lai_suat_3thang)))
so_luong_nhan_vien1=chuyen_dac_truong_sang_so_co_Null(da.so_luong_nhan_vien, ganSoPhanLoai(xoaTrung(da.so_luong_nhan_vien)))



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

# tao tap  du lieu x_training co loc du lieu unknown
for i in range(len(tuoi)):
    x_training_coLoc.append([
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
i=len(x_training_coLoc)-1
while i>=0:
    if(i<len(x_training_coLoc)):
        for j in x_training_coLoc[i]:
            if j is None:
                x_training_coLoc.pop(i)
    i-=1
# tao tap du lieu y_training
y_training=da.label
# tao bien tra cuu thong tin
traCuu.append(['tuoi: 0'])
traCuu.append(['nghe_nghiep: 1'])
traCuu.append(['hon_nhan: 2'])
traCuu.append(['hoc_van: 3'])
traCuu.append(['co_the_tin_dung: 4'])
traCuu.append(['co_nha_o: 5'])
traCuu.append(['vay_ca_nhan: 6'])
traCuu.append(['kenh_lien_lac: 7'])
traCuu.append(['thang_lien_lac: 8'])
traCuu.append(['ngay_lien_lac: 9'])
traCuu.append(['thoi_luong_lien_lac: 10'])
traCuu.append(['so_luong_lien_lac: 11'])
traCuu.append(['ngay: 12'])
traCuu.append(['so_luong_lien_lac_truoc_day: 13'])
traCuu.append(['ket_qua_lan_truoc: 14'])
traCuu.append(['ti_le_thay_doi_viec_lam: 15'])
traCuu.append(['CPI: 16'])
traCuu.append(['CCI: 17'])
traCuu.append(['lai_suat_3thang: 18'])
traCuu.append(['so_luong_nhan_vien: 19'])

print("\t\t\t\t 2 -> Xử lý dữ liệu thành công!")
