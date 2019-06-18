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
def Mean(dt):
    #tinh ki vong trung binh
    print(dt[0])
    mean_vec = np.mean(dt, axis=0)
    print(mean_vec[0])
    return mean_vec
def Draw_2d(k,title):
    X_pc = stepwise_kpca(k, gamma=1, n_components=2)

    #plt.scatter(X_pc[:, 0], X_pc[:, 1], c=label_(k))
    y = label_(k)
    plt.scatter(X_pc[y == 0, 0], X_pc[y == 0, 1], color='red', alpha=0.5)
    plt.scatter(X_pc[y == 1, 0], X_pc[y == 1, 1], color='blue', alpha=0.5)
    plt.ylabel("PC2")
    plt.xlabel("PC1")
    plt.title(title)
    plt.show()
Draw_2d(2,'Gaussian RBF kernel PCA')