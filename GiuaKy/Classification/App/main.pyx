import sys
sys.path.append('../BUS/')
import knn

def KNN():
    #knn.help()
    print(u"\t\t\tKnn bắt đầu chạy:")
    kq0=knn.ketQua(0)
    kq1=knn.ketQua(1)
    knn.Ve2D(0,['hoc_van','nghe_nghiep'],50)
    knn.Ve3D(1,['hoc_van','nghe_nghiep','thoi_luong_lien_lac'],100)
