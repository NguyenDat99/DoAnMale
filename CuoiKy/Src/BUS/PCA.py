#dataset(3) -> dataset_for_PCA_LDA
import sys
sys.path.append('../DAO/')
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
import DataProcessing as dp
import plotly.plotly as py
from sklearn.preprocessing import StandardScaler
import numpy as np
# thu vien ve cua python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# thu vien sklearn cho ho tro knn
from sklearn.neighbors import KNeighborsClassifier
#Đánh giá
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()

# k y nghia la chon dataset cho tap iris hoac dataset goc

def data(k):
    if k==1:
        return dp.data(3)
    elif k==2:
        return iris.data
def label_(k):
    if k==1:
        return dp.label_(3)
    elif k==2:
        return iris.target
def Standardizing(k):
    #chuan hoa du lieu
    dt = StandardScaler().fit_transform(data(k))
    return dt
def Mean(dt):
    #tinh ki vong trung binh
    print(dt[0])
    mean_vec = np.mean(dt, axis=0)
    print(mean_vec[0])
    return mean_vec


def CovarianceMatrix(dt,mean_vec):
    #tinh matrix hiep phuong sai
    #σjk=1n−1∑Ni=1(xij−x¯j)(xik−x¯k)
    cov_mat = (dt - mean_vec).T.dot((dt - mean_vec)) / (dt.shape[0]-1)
    return cov_mat

def Eigen_Values(k):
    dt=Standardizing(k)
    mean_vec=Mean(dt)
    cov_mat=CovarianceMatrix(dt,mean_vec)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    return eig_vals

def Eigen_Vectors(k):
    dt=Standardizing(k)
    mean_vec=Mean(dt)
    cov_mat=CovarianceMatrix(dt,mean_vec)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    return eig_vecs

def Selecting_Pri_Components(k):
    if k==2:
        return None
    eig_vals=Eigen_Values(k)
    eig_vecs=Eigen_Vectors(k)
    eig = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    # xap xep eigenvalue, eigenvector tuples tu cao den thap
    eig.sort()
    eig.reverse()
    ##danh gia du lieu bi mat
    s = sum(eig_vals)
    var = [(i / s)*100 for i in sorted(eig_vals, reverse=True)]
    csvar = np.cumsum(var)
    ##ve
    y=[(i+50,csvar[i])for i in range(11)]
    y=np.array(y)
    plt.scatter(y[:,0],y[:,1],marker="*",c="red")
    for i in range(11):
        plt.text(float(y[i,0])+0.3,float(y[i,1])-0.3,"PC%s"%i,fontsize=15)
    plt.plot(y[:,0],y[:,1])
    plt.ylabel("Độ chính xác(%)")
    plt.title("Biểu đồ thể hiện lượng thông tin của các PC")
    plt.show()


def new_Data(n_pc,k):
    dt=Standardizing(k)
    eig_vals=Eigen_Values(k)
    eig_vecs=Eigen_Vectors(k)
    eig = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    # xap xep eigenvalue, eigenvector tuples tu cao den thap
    eig.sort()
    eig.reverse()
    ##danh gia du lieu bi mat
    s = sum(eig_vals)
    var = [(i / s)*100 for i in sorted(eig_vals, reverse=True)]
    csvar = np.cumsum(var)
    tmp=[]
    for i in range(n_pc):
        tmp.append(eig[i][1])
    tmp=np.array(tmp)
    #Y=X*W
    Y = dt.dot(tmp.T)
    return Y


def KNN(n_pc,k):
    x_train, x_test, y_train, y_test=train_test_split(
    data(k),label_(k),test_size=0.2)
    dt=new_Data(n_pc,k)
    if k==2:
        return None
    x_train_PCA, x_test_PCA, y_train_PCA, y_test_PCA=train_test_split(
    dt,label_(k),test_size=0.2)
    clf=KNeighborsClassifier(n_neighbors=13).fit(x_train,y_train)
    precision= precision_score(y_test,clf.predict(x_test))
    recall= recall_score(y_test,clf.predict(x_test))
    F=(2*precision*recall)/(precision+recall)
    clf1=KNeighborsClassifier(n_neighbors=13).fit(x_train_PCA,y_train_PCA)
    precision1= precision_score(y_test_PCA,clf1.predict(x_test_PCA))
    recall1= recall_score(y_test_PCA,clf1.predict(x_test_PCA))
    F1=(2*precision1*recall1)/(precision1+recall1)
    return [F,F1]


def Draw_2d(k,title):
    dt=new_Data(2,k)
    dt=np.array(dt)
    plt.scatter(dt[:,0],dt[:,1],c=label_(k))
    plt.ylabel("Y")
    plt.xlabel("x")
    plt.title(title)
    plt.show()

def Draw_3d(k,title):
    dt=new_Data(3,k)
    fig = plt.figure()
    dt=np.array(dt)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dt[:,0],dt[:,1],dt[:,2],c=label_(k),s=100)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title(title)
    plt.show()