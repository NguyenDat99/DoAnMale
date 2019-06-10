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
# thu vien thuan toan LinearRegression
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
from mpl_toolkits.mplot3d import Axes3D

data=dp.data(2)
label_=dp.label_(2)




def MR(x_train,y_train,x_test,y_test):
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)
    score=r2_score(y_test,y_pred)
    k=[]
    k.append([score,y_pred])
    return np.array(k)


def vitriDacTrung(dacTrung):
    if dacTrung=='Age':
        return 0
    elif dacTrung=='Weight':
        return 1
    elif dacTrung=='Height':
        return 2
    elif dacTrung=='Neck':
        return 3
    elif dacTrung=='Chest':
        return 4
    elif dacTrung=='Abdomen':
        return 5
    elif dacTrung=='Hip':
        return 6
    elif dacTrung=='Thigh':
        return 7
    elif dacTrung=='Knee':
        return 8
    elif dacTrung=='Ankle':
        return 9
    elif dacTrung=='Biceps':
        return 10
    elif dacTrung=='Forearm':
        return 11
    elif dacTrung=='Wrist':
        return 12

def tenDacTrung(viTri):
      switcher={
                0:'Age',
                1:'Weight',
                2:'Height',
                3:'Neck',
                4:'Chest',
                5:'Abdomen',
                6:'Hip',
                7:'Thigh',
                8:'Knee',
                9:'Ankle',
                10:'Biceps',
                11:'Forearm',
                12:'Wrist'
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
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    m1=MR(x_train[layviTriDacTrung(dacTrungVe)],y_train,x_test[layviTriDacTrung(dacTrungVe)],y_test)
    y_pred=[]
    for i in range(len((m1[:,1])[0])):
        y_pred.append((m1[:,1])[0][i])
    plt.scatter(x_test[layviTriDacTrung(dacTrungVe)],y_test,s=10,c="#3366cc")
    plt.plot(x_test[layviTriDacTrung(dacTrungVe)],y_pred, color='#cc0099', linewidth=3)
    plt.xlabel("%s(Xj)"%dacTrungVe)
    plt.ylabel('Y')
    plt.show()

def ve3D(mangCacDacTrung,dacTrungVe):
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    m0=MR(x_train[layviTriDacTrung([dacTrungVe[0]])],y_train,x_test[layviTriDacTrung([dacTrungVe[0]])],y_test)
    m1=MR(x_train[layviTriDacTrung([dacTrungVe[1]])],y_train,x_test[layviTriDacTrung([dacTrungVe[1]])],y_test)
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
    return float(MR(x_train,y_train,x_test,y_test)[:,0])*100

#ve2D(['Age','Weight','Height'],['Weight'])
#ve3D(['Age','Weight','Height'],['Age','Weight'])
#print(tinhToan(['Age','Weight','Height']))
