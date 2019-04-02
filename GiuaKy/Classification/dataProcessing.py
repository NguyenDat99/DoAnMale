# coding=utf-8
import pandas as pd
import layDataset as ld
x_training=[]#tap du lieu training da duoc bien doi
y_training=[]#label cho tap du lieu x_training
#luu gia tri cu (truoc khi bien doi) va gia tri moi sau khi bien doi
class bangAnhXa:
    def __init__(self,giatriCu,giatriMoi):
        self.giatriCu=giatriCu
        self.giatriMoi=giatriMoi
#xoa phan tu trung lap
def xoaTrung(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    for i in range(len(b)):
        if b[i]=='unknown':
            b[0],b[i]=b[i],b[0]
    return b
#chuyen doi qua so cho cac gia tri da xoa trung
def ganSoPhanLoai(mangXoaTrung):
    b=[]
    for i in range(len(mangXoaTrung)):
        b.append([mangXoaTrung[i],i])
    return b
#chuyen cac dac trung ban dau thanh dang so
def chuyen_dac_truong_sang_so(dac_trung_cu,mang_ganSoPhanLoai):
    a=[]
    for i in dac_trung_cu:
        for j in mang_ganSoPhanLoai:
            if i==j[0]:
                a.append([j[1]])
    return a;
tuoi=chuyen_dac_truong_sang_so(ld.tuoi, ganSoPhanLoai(xoaTrung(ld.tuoi)))
