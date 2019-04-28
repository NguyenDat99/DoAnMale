import knn

def KNN():
    #knn.help()
    kq0=knn.ketQua(0)
    kq1=knn.ketQua(1)
    print(u"\tDữ liệu có lọc:")
    print(kq0.weights)
    print(kq0.n_neighbors)
    print(kq0.F)
    print(u"\tDữ liệu không lọc:")
    print(kq1.weights)
    print(kq1.n_neighbors)
    print(kq1.F)
    knn.Ve2D(0,['hoc_van','nghe_nghiep'],50)
    knn.Ve3D(1,['hoc_van','nghe_nghiep','thoi_luong_lien_lac'],50)
