

#dataset(0) -> dataset_for_Kernel_PCA
#dataset(1) -> dataset_for_Logistic_regression
#dataset(2) -> dataset_for_MultiLinear_regression
#dataset(3) -> dataset_for_PCA_LDA
#dataset(4) -> dataset_for_Poly_regression

# coding=utf-8
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool


dataset_for_Kernel_PCA=pd.read_csv('../DTO/dataset/dataset_for_Kernel_PCA.csv',encoding='utf-8')
dataset_for_Logistic_regression=pd.read_csv('../DTO/dataset/dataset_for_Logistic_regression.csv',encoding='utf-8')
dataset_for_MultiLinear_regression=pd.read_csv('../DTO/dataset/dataset_for_MultiLinear_regression.csv',encoding='utf-8')
dataset_for_PCA_LDA=pd.read_csv('../DTO/dataset/dataset_for_PCA_LDA.csv',encoding='utf-8')
dataset_for_Poly_regression=pd.read_csv('../DTO/dataset/dataset_for_Poly_regression.csv',encoding='utf-8')






# lay dataset tu file  len va cung cap method lay tung cot tuong ung cua dataset do
def get_dataset_for_Kernel_PCA(name):
    return (dataset_for_Kernel_PCA[name].values).tolist()

def get_dataset_for_Logistic_regression(name):
    return  (dataset_for_Logistic_regression[name].values).tolist()

def get_dataset_for_MultiLinear_regression(name):
    return (dataset_for_MultiLinear_regression[name].values).tolist()

def get_dataset_for_PCA_LDA(name):
    return (dataset_for_PCA_LDA[name].values).tolist()

def get_dataset_for_Poly_regression(name):
    return (dataset_for_Poly_regression[name].values).tolist()



def multiprocessing(k):
    if k==0:#dataset_for_Kernel_PCA
        t=['User ID','Gender','Age','EstimatedSalary','Purchased']
        pool = ThreadPool(4)
        data=pool.map(get_dataset_for_Kernel_PCA,t)
    elif k==1:#dataset_for_Logistic_regression
        t=['Sex','AgeRange','Class_','SiblingSpouse','ParentChild','Embarked_','Survived']
        pool = ThreadPool(4)
        data=pool.map(get_dataset_for_Logistic_regression,t)
    elif k== 2: #dataset_for_MultiLinear_regression:
        t=['Age','Weight','Height','Neck','Chest','Abdomen','Hip','Thigh','Knee','Ankle','Biceps','Forearm','Wrist','FAT_PER']#dataset_for_MultiLinear_regression
        pool = ThreadPool(4)
        data=pool.map(get_dataset_for_MultiLinear_regression,t)
    elif k==3:#dataset_for_PCA_LDA
        t=['LOC_BLANK',	'BRANCH_COUNT',	'CALL_PAIRS','LOC_CODE_AND_COMMENT','LOC_COMMENTS','CONDITION_COUNT','CYCLOMATIC_COMPLEXITY','CYCLOMATIC_DENSITY','DECISION_COUNT','DECISION_DENSITY','DESIGN_COMPLEXITY','DESIGN_DENSITY','EDGE_COUNT','ESSENTIAL_COMPLEXITY','ESSENTIAL_DENSITY','LOC_EXECUTABLE','PARAMETER_COUNT','GLOBAL_DATA_COMPLEXITY','GLOBAL_DATA_DENSITY','HALSTEAD_CONTENT','HALSTEAD_DIFFICULTY','HALSTEAD_EFFORT','HALSTEAD_ERROR_EST',	'HALSTEAD_LENGTH','HALSTEAD_LEVEL','HALSTEAD_PROG_TIME','HALSTEAD_VOLUME','MAINTENANCE_SEVERITY','MODIFIED_CONDITION_COUNT','MULTIPLE_CONDITION_COUNT','FAILDE_COUNT','FAILRMALIZED_CYLOMATIC_COMPLEXITY','NUM_OPERANDS','NUM_OPERATORS','NUM_UNIQUE_OPERANDS','NUM_UNIQUE_OPERATORS','NUMBER_OF_LINES','PERCENT_COMMENTS','LOC_TOTAL','TEST_RESULT']#dataset_for_PCA_LDA
        pool = ThreadPool(4)
        data=pool.map(get_dataset_for_PCA_LDA,t)
    elif k==4:#dataset_for_Poly_regression
        t=['Rating',	'Reviews',	'Size',	'Installs']
        pool = ThreadPool(4)
        data=pool.map(get_dataset_for_Poly_regression,t)
    return data


#dataset(0) -> dataset_for_Kernel_PCA
#dataset(1) -> dataset_for_Logistic_regression
#dataset(2) -> dataset_for_MultiLinear_regression
#dataset(3) -> dataset_for_PCA_LDA
#dataset(4) -> dataset_for_Poly_regression

class dataset:
    def __init__(seft,k):
        data=multiprocessing(k)
        if k==0:
            seft.User_ID=data[0]
            seft.Gender=data[1]
            seft.Age=data[2]
            seft.EstimatedSalary=data[3]
            seft.Purchased =data[4]
        elif k==1:
            seft.Sex=data[0]
            seft.AgeRange=data[1]
            seft.Class_=data[2]
            seft.SiblingSpouse=data[3]
            seft.ParentChild=data[4]
            seft.Embarked_=data[5]
            seft.Survived=data[6]
        elif k==2:
            seft.Age=data[0]
            seft.Weight=data[1]
            seft.Height=data[2]
            seft.Neck=data[3]
            seft.Chest=data[4]
            seft.Abdomen=data[5]
            seft.Hip=data[6]
            seft.Thigh=data[7]
            seft.Knee=data[8]
            seft.Ankle=data[9]
            seft.Biceps=data[10]
            seft.Forearm=data[11]
            seft.Wrist=data[12]
            seft.FAT_PER=data[13]

        elif k==3:
            seft.LOC_BLANK=data[0]
            seft.BRANCH_COUNT=data[1]
            seft.CALL_PAIRS=data[2]
            seft.LOC_CODE_AND_COMMENT=data[3]
            seft.LOC_COMMENTS=data[4]
            seft.CONDITION_COUNT=data[5]
            seft.CYCLOMATIC_COMPLEXITY=data[6]
            seft.CYCLOMATIC_DENSITY=data[7]
            seft.DECISION_COUNT=data[8]
            seft.DECISION_DENSITY=data[9]
            seft.DESIGN_COMPLEXITY=data[10]
            seft.DESIGN_DENSITY=data[11]
            seft.EDGE_COUNT=data[12]
            seft.ESSENTIAL_COMPLEXITY=data[13]
            seft.ESSENTIAL_DENSITY=data[14]
            seft.LOC_EXECUTABLE=data[15]
            seft.PARAMETER_COUNT=data[16]
            seft.GLOBAL_DATA_COMPLEXITY=data[17]
            seft.GLOBAL_DATA_DENSITY=data[18]
            seft.HALSTEAD_CONTENT=data[19]
            seft.HALSTEAD_DIFFICULTY=data[20]
            seft.HALSTEAD_EFFORT=data[21]
            seft.HALSTEAD_ERROR_EST=data[22]
            seft.HALSTEAD_LENGTH=data[23]
            seft.HALSTEAD_LEVEL=data[24]
            seft.HALSTEAD_PROG_TIME=data[25]
            seft.HALSTEAD_VOLUME=data[26]
            seft.MAINTENANCE_SEVERITY=data[27]
            seft.MODIFIED_CONDITION_COUNT=data[28]
            seft.MULTIPLE_CONDITION_COUNT=data[29]
            seft.FAILDE_COUNT=data[30]
            seft.FAILRMALIZED_CYLOMATIC_COMPLEXITY=data[31]
            seft.NUM_OPERANDS=data[32]
            seft.NUM_OPERATORS=data[33]
            seft.NUM_UNIQUE_OPERANDS=data[34]
            seft.NUM_UNIQUE_OPERATORS=data[35]
            seft.NUMBER_OF_LINES=data[36]
            seft.PERCENT_COMMENTS=data[37]
            seft.LOC_TOTAL=data[38]
            seft.TEST_RESULT=data[39]
        elif k==4:
            seft.Rating=data[0]
            seft.Reviews=data[1]
            seft.Size=data[2]
            seft.Installs=data[3]
