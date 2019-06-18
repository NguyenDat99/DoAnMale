#dataset(0) -> dataset_for_Kernel_PCA
#dataset(1) -> dataset_for_Logistic_regression
#dataset(2) -> dataset_for_MultiLinear_regression
#dataset(3) -> dataset_for_PCA_LDA
#dataset(4) -> dataset_for_Poly_regression
import sys
sys.path.append('../DAO/')
# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
import DataProcessing as dp
import operator
# thu vien thuan toan LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# danh gia
from sklearn.metrics import r2_score
#chon dac trung dung cay quyet dinh
from sklearn import tree
#chuyen sang anh
import pydotplus
#xu ly matrix
import numpy as np
# thu vien ve cua python
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import make_pipeline
from mpl_toolkits.mplot3d import Axes3D

data=dp.data(4)
label_=dp.label_(4)

def PLR(x_train,y_train,x_test,y_test):
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(x_train)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y_train)
    X_poly1 = poly_reg.fit_transform(x_test)
    y_pred = lin_reg_2.predict(X_poly1)
    score = r2_score(y_test, y_pred)
    k=[]
    k.append([score,y_pred])
    return np.array(k)



def vitriDacTrung(dacTrung):
    if dacTrung=='Rating':
        return 0
    elif dacTrung=='Reviews':
        return 1
    elif dacTrung=='Size':
        return 2
def tenDacTrung(viTri):
      switcher={
                0:'Rating',
                1:'Reviews',
                2:'Size'
                }
      return switcher.get(viTri)

def layviTriDacTrung(mangCacDacTrung):
    m=[]
    for i in mangCacDacTrung:
        m.append(vitriDacTrung(i))
    return m

def layDacTrung(mangCacDacTrung):
    return pd.DataFrame(data)[layviTriDacTrung(mangCacDacTrung)]


def ve2D(mangCacDacTrung,dacTrungVe):
    x_train,x_test,y_train,y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    m1=PLR(x_train[layviTriDacTrung(dacTrungVe)],y_train,x_test[layviTriDacTrung(dacTrungVe)],y_test)
    y_pred=[]
    for i in range(len((m1[:,1])[0])):
        y_pred.append((m1[:,1])[0][i])

    # pr = LinearRegression()
    # quadratic = PolynomialFeatures(degree=2)
    # X_quad = quadratic.fit_transform(x_train[layviTriDacTrung(dacTrungVe)])
    # pr.fit(X_quad, y_train)
    # y_quad_fit = pr.predict(quadratic.fit_transform(x_test[layviTriDacTrung(dacTrungVe)]))

    plt.scatter(x_train[layviTriDacTrung(dacTrungVe)],y_train,s=10,c='blue')
    plt.plot(x_test[layviTriDacTrung(dacTrungVe)],y_pred, color='red')
    plt.title('Polynomial Regression')
    plt.xlabel("%s(Xj)"%dacTrungVe)
    plt.ylabel('Y')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


def ve3D(mangCacDacTrung,dacTrungVe):
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    m0=PLR(x_train[layviTriDacTrung([dacTrungVe[0]])],y_train,x_test[layviTriDacTrung([dacTrungVe[0]])],y_test)
    m1=PLR(x_train[layviTriDacTrung([dacTrungVe[1]])],y_train,x_test[layviTriDacTrung([dacTrungVe[1]])],y_test)
    y_pred0=[]
    y_pred1=[]
    for i in range(len((m0[:,1])[0])):
        y_pred0.append((m0[:,1])[0][i])
    for i in range(len((m1[:,1])[0])):
        y_pred1.append((m1[:,1])[0][i])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(y_test,x_test[layviTriDacTrung([dacTrungVe[0]])],x_test[layviTriDacTrung([dacTrungVe[1]])])
    ax.plot(x_test[layviTriDacTrung([dacTrungVe[0]])], y_pred0)
    ax.plot(x_test[layviTriDacTrung([dacTrungVe[1]])], y_pred1)
    plt.show()


def tinhToan(mangCacDacTrung):
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    return float(PLR(x_train,y_train,x_test,y_test)[:,0])*100

ve2D(['Rating','Reviews','Size'],['Reviews'])
#ve2D(['Age','Weight','Height'],['Weight'])
ve3D(['Rating','Reviews','Size'],['Rating','Size'])
print(tinhToan(['Rating','Reviews','Size']))
#print(tinhToan(['Age','Weight','Height']))
