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
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

data=dp.data(1)
label_=dp.label_(1)

#x_train, x_test, y_train, y_test = train_test_split(dp.data, dp.label_, test_size=0.25, random_state=0)

#clf = LogisticRegression(random_state=0, solver='lbfgs',
#                         multi_class='multinomial')
#clf.fit(x_train,y_train)
#y_pred =  clf.predict(x_test)
#print('\nAccuracy = ',accuracy_score(y_test, y_pred))
#print('\nClassification report\n')
#print(classification_report(y_test, y_pred))

def logistic(x_train,y_train,x_test,y_test):
    logic = LogisticRegression()
    logic.fit(x_train, y_train)
    y_pred = logic.predict(x_test)
    score=r2_score(y_test,y_pred)
    k=[]
    k.append([score,y_pred])
    return np.array(k)

def vitriDacTrung(dacTrung):
    if dacTrung=='Sex':
        return 0
    elif dacTrung=='AgeRange':
        return 1
    elif dacTrung=='Class_':
        return 2
    elif dacTrung=='SiblingSpouse':
        return 3
    elif dacTrung=='ParentChild':
        return 4
    elif dacTrung=='Embarked_':
        return 5

def tenDacTrung(viTri):
      switcher={
                0:'Sex',
                1:'AgeRange',
                2:'Class_',
                3:'SiblingSpouse',
                4:'ParentChild',
                5:'Embarked_',
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
    m1=logistic(x_train[layviTriDacTrung(dacTrungVe)],y_train,x_test[layviTriDacTrung(dacTrungVe)],y_test)
    y_pred=[]
    for i in range(len((m1[:,1])[0])):
        y_pred.append((m1[:,1])[0][i])
    plt.scatter(x_test[layviTriDacTrung(dacTrungVe)],y_test,s=10,c="#3366cc")
    plt.plot(x_test[layviTriDacTrung(dacTrungVe)],y_pred, color='#cc0099', linewidth=3)
    plt.xlabel("%s(Xj)"%dacTrungVe)
    plt.ylabel('Y')
    plt.show()
    
def tinhToan(mangCacDacTrung):
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    return float(logistic(x_train,y_train,x_test,y_test)[:,0])*100





def ve3D(mangCacDacTrung,dacTrungVe):
    x_train, x_test, y_train, y_test=train_test_split(layDacTrung(mangCacDacTrung),label_,test_size=0.2)
    m0=logistic(x_train,y_train,x_test,y_test)
    y_pred0=[]
    for i in range(len((m0[:,1])[0])):
        y_pred0.append((m0[:,1])[0][i])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_test[layviTriDacTrung([dacTrungVe[0]])],x_test[layviTriDacTrung([dacTrungVe[1]])],y_test)
    ax.plot(x_test[layviTriDacTrung([dacTrungVe[0]])],x_test[layviTriDacTrung([dacTrungVe[1]])], y_pred0)
    plt.show()

ve2D(['Sex','AgeRange','Class_','SiblingSpouse','ParentChild','Embarked_'],['ParentChild'])
#ve3D(['Sex','AgeRange','Class_','SiblingSpouse','ParentChild','Embarked_'],['ParentChild','Embarked_'])
print(tinhToan(['Sex','AgeRange','Class_','SiblingSpouse','ParentChild','Embarked_']))