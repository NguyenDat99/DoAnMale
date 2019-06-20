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
dataset = dp.data(3)
label_=dp.label_(3)

def data(k):
    tmp=[]
    if k==0:
        for i in range(len(dataset)):
            if label_[i]==0:
                    tmp.append(dataset[i])
    elif k==1:
        for i in range(len(dataset)):
            if label_[i]==1:
                    tmp.append(dataset[i])
    elif k==2:
        tmp=dataset
    return tmp

def Standardizing(k):
    #chuan hoa du lieu
    dt = StandardScaler().fit_transform(data(k))
    return dt

def Mean(dt):
    #tinh ki vong trung binh tuong ung voi tung class
    mean_vec = np.mean(dt, axis=0)
    return mean_vec



def Sw():
    #Σi=1Ni−1∑xx∈Din(xx−mmi)(xx−mmi)T.
    dt0=Standardizing(0)
    dt1=Standardizing(1)
    mean_vec0=Mean(dt0)
    mean_vec1=Mean(dt1)
    a = (dt0 - mean_vec0).T.dot((dt0 - mean_vec0))
    b=  (dt1 - mean_vec1).T.dot((dt1 - mean_vec1))
    return a+b

def Sb():
    dt=Standardizing(2)
    mean=Mean(dt)
    dt0=Standardizing(0)
    dt1=Standardizing(1)
    mean_vec0=Mean(dt0)
    mean_vec1=Mean(dt1)
    a = (mean_vec0-mean).dot((mean_vec0-mean).T)*(dt0.shape[0])
    b = (mean_vec1-mean).dot((mean_vec1-mean).T)*(dt1.shape[0])
    return a+b


def LDA_matrix():
    m=np.linalg.inv(Sw()).dot(Sb())
    return m




def Eigen_Values():
    LDA_mat=LDA_matrix()
    eig_vals, eig_vecs = np.linalg.eig(LDA_mat)
    return eig_vals


def Eigen_Vectors():
    LDA_mat=LDA_matrix()
    eig_vals, eig_vecs =np.linalg.eig(LDA_mat)
    return eig_vecs



def new_Data(n_pc):
    eig_vals=Eigen_Values()
    eig_vecs=Eigen_Vectors()
    eig = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    # xap xep eigenvalue, eigenvector tuples tu cao den thap
    eig.sort()
    eig.reverse()
    tmp=[]
    for i in range(n_pc):
        tmp.append(eig[i][1])
    tmp=np.array(tmp)
    Y = Standardizing(2).dot(tmp.T)
    return Y



def Selecting_Pri_Components():
    eig_vals=Eigen_Values()
    eig_vecs=Eigen_Vectors()
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
    plt.scatter(y[:,0],y[:,1],marker="o",c="#ff0066")
    plt.plot(y[:,0],y[:,1],c="#3366cc")
    plt.ylabel("Độ chính xác(%)")
    plt.title("Biểu đồ thể hiện lượng thông tin của các LD")
    plt.show()



def KNN(n_pc):
    x_train, x_test, y_train, y_test=train_test_split(
    Standardizing(2),label_,test_size=0.2)
    dt=new_Data(n_pc)
    x_train_LDA, x_test_LDA, y_train_LDA, y_test_LDA=train_test_split(
    dt,label_,test_size=0.2)
    clf=KNeighborsClassifier(n_neighbors=13).fit(x_train,y_train)
    precision= precision_score(y_test,clf.predict(x_test))
    recall= recall_score(y_test,clf.predict(x_test))
    F=(2*precision*recall)/(precision+recall)
    clf1=KNeighborsClassifier(n_neighbors=13).fit(x_train_LDA,y_train_LDA)
    precision1= precision_score(y_test_LDA,clf1.predict(x_test_LDA))
    recall1= recall_score(y_test_LDA,clf1.predict(x_test_LDA))
    F1=(2*precision1*recall1)/(precision1+recall1)
    return [F,F1]


def Draw_2d(title):
    dt=new_Data(2)
    dt=np.array(dt)
    plt.scatter(dt[:,0],dt[:,1],c=label_)
    plt.ylabel("Y")
    plt.xlabel("x")
    plt.title(title)
    plt.show()


def Draw_3d(title):
    dt=new_Data(3)
    fig = plt.figure()
    dt=np.array(dt)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dt[:,0],dt[:,1],dt[:,2],c=label_,s=100)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title(title)
    plt.show()
