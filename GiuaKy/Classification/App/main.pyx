import sys
sys.path.append('../BUS/')
import knn

def KNN():
    #knn.help()
    print(u"\t\t\tKnn bắt đầu chạy:")
    kq0=knn.ketQua(0)
    kq1=knn.ketQua(1)
    print("du lieu loc: ")
    print("weights=%s"%kq0.weights)
    print("n_neighbors=%s"%kq0.n_neighbors)
    print("F=%s"%kq0.F)
    print("du lieu khong loc:")
    print("weights=%s"%kq1.weights)
    print("n_neighbors=%s"%kq1.n_neighbors)
    print("F=%s"%kq1.F)
    knn.Ve2D(0,['hoc_van','nghe_nghiep'],50)
    knn.Ve3D(1,['hoc_van','nghe_nghiep','thoi_luong_lien_lac'],100)

KNN()
