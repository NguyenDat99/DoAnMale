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
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np

def data(k):
    if k==1:
        return dp.data(0)
    elif k==2:
        return iris.data
def label_(k):
    if k==1:
        return dp.label_(0)
    elif k==2:
        return iris.target
def Standardizing(k):
    #chuan hoa du lieu
    dt = StandardScaler().fit_transform(data(k))
    return dt
#Implementing the RBF kernel PCA step-by-step
def stepwise_kpca(X, gamma, n_components):
    """
    Implementation of a RBF kernel PCA.

    Arguments:
        X: A MxN dataset as NumPy array where the samples are stored as rows (M),
           and the attributes defined as columns (N).
        gamma: A free parameter (coefficient) for the RBF kernel.
        n_components: The number of components to be returned.

    """
    # Calculating the squared Euclidean distances for every pair of points
    # in the MxN dimensional dataset.
    sq_dists = pdist(Standardizing(X), 'sqeuclidean')

    # Converting the pairwise distances into a symmetric MxM matrix.
    mat_sq_dists = squareform(sq_dists)

    # Computing the MxM kernel matrix.
    K = exp(-gamma * mat_sq_dists)

    # Centering the symmetric NxN kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigvals, eigvecs = eigh(K)

    # Obtaining the i eigenvectors that corresponds to the i highest eigenvalues.
    X_pc = np.column_stack((eigvecs[:,-i] for i in range(1,n_components+1)))
    return X_pc

def Eigen_Values(X, gamma):
    sq_dists = pdist(Standardizing(X), 'sqeuclidean')

    # Converting the pairwise distances into a symmetric MxM matrix.
    mat_sq_dists = squareform(sq_dists)

    # Computing the MxM kernel matrix.
    K = exp(-gamma * mat_sq_dists)

    # Centering the symmetric NxN kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigvals, eigvecs = eigh(K)
    return eigvals

def Eigen_Vectors(X, gamma):
    sq_dists = pdist(Standardizing(X), 'sqeuclidean')

    # Converting the pairwise distances into a symmetric MxM matrix.
    mat_sq_dists = squareform(sq_dists)

    # Computing the MxM kernel matrix.
    K = exp(-gamma * mat_sq_dists)

    # Centering the symmetric NxN kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenvalues in descending order with corresponding
    # eigenvectors from the symmetric matrix.
    eigvals, eigvecs = eigh(K)
    return eigvecs
def Selecting_Pri_Components(k):
    if k==2:
        return None
    eig_vals=Eigen_Values(k,0.1)
    eig_vecs=Eigen_Vectors(k,0.1)
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

def KNN(gamma,k,n_comp):
    x_train, x_test, y_train, y_test=train_test_split(
    data(k),label_(k),test_size=0.2)
    dt=stepwise_kpca(k,gamma,n_comp)
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

def Draw_2d(k,title,gamma):
    X_pc = stepwise_kpca(k, gamma=gamma, n_components=2)

    #convert string
    x=str(gamma)

    #Plot drawing
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pc[:, 0], X_pc[:, 1], c=label_(k))
    y = label_(k)
    plt.ylabel("PC2")
    plt.xlabel("PC1")
    plt.title(title+' gamma='+x )
    plt.show()

# print('Eigen_Values:', Eigen_Values(1,0.2))
# print('Eigen_Vectors:', Eigen_Vectors(1,0.2))
# Selecting_Pri_Components(2)
print(KNN(0.2,1,2))
#Draw_2d(1,'Gaussian RBF kernel PCA',0.2)