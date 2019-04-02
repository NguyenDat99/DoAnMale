import dataProcessing as dp# tap du lieu su dung
import matplotlib.pyplot as plt # thu vien ve cua python
from sklearn.neighbors import KNeighborsClassifier # thu vien sklearn cho ho tro knn
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

# chia tap du lieu ban dau thanh 2 tap la training va testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(dp.x_training_notNull,dp.y_training,test_size=0.3)

clf=KNeighborsClassifier(n_neighbors=89).fit(x_train,y_train)
precision= precision_score(y_test,clf.predict(x_test))
recall= recall_score(y_test,clf.predict(x_test))
print(recall)
#print(x_train)
