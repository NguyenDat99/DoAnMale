import sys
sys.path.append('../BUS/')
import knn
import svm
import naiveBayes as nb
import svmKernel as svk

def KNN():
    #knn.help()
    print(u"\t\t\tKnn bắt đầu chạy:")
    #kq0=knn.ketQua(0)
    kq1=knn.ketQua(1)
    knn.Ve2D(0,['hoc_van','nghe_nghiep'],50)
    knn.Ve3D(1,['hoc_van','nghe_nghiep','thoi_luong_lien_lac'],100)


def SVM():
    svm.svcloc()
    svm.svckloc()
    svm.linearloc()
    svm.linearkloc()
    svm.gridsvc()
    svm.gridsvc1()

def SVM_Kelnels():
    svk.ketQua()
    svk.ve()

def NB():
  nb.gauloc()
  nb.gaukloc()
  nb.mulloc()
  nb.mulkloc()
  nb.berloc()
  nb.berkloc()
