
#dataset(0) -> dataset_for_Kernel_PCA
#dataset(1) -> dataset_for_Logistic_regression
#dataset(2) -> dataset_for_MultiLinear_regression
#dataset(3) -> dataset_for_PCA_LDA
#dataset(4) -> dataset_for_Poly_regression


# coding=utf-8
# thu vien xu ly duong dan
import sys
sys.path.append('../DTO/')
import DataAdapter as da


def locKyTu(k):
    s=""
    for i in k:
        if i!=',' and i !='+':
            s+=i
    return int(s)


def chuyenDoiDuLieu(k):
    s=""
    for i in k:
        if i!='M' and i!='k':
            s+=i
    if k[len(k)-1]=='k':
        return float(s)*1000
    elif k[len(k)-1]=='M':
        return float(s)*1000000

def data(k):
    dt=[]
    tmp=da.dataset(k)
    if k==0:# dataset_for_Kernel_PCA
        dem=0
        for i in range(len(tmp.User_ID)):
            if tmp.Gender[i]=='Male':
                dt.append([dem,0,tmp.Age[i],
                tmp.EstimatedSalary[i]/1000,tmp.Purchased[i]])
            elif  tmp.Gender[i]=='Female':
                dt.append([dem,1,tmp.Age[i],
                tmp.EstimatedSalary[i]/1000,tmp.Purchased[i]])
            dem+=1
    elif k==1:# dataset_for_Logistic_regression
        Sex=0
        AgeRange=0
        Class_=0
        Embarked_=0
        for i in range(len(tmp.Sex)):
            if tmp.Sex[i]=='Male':
                Sex=0
            elif tmp.Sex[i]=='Female':
                Sex=1
            if tmp.AgeRange[i]=='Age_0_9':
                AgeRange=0
            elif tmp.AgeRange[i]=='Age_10_19':
                AgeRange=1
            elif tmp.AgeRange[i]=='Age_20_29':
                AgeRange=2
            elif tmp.AgeRange[i]=='Age_30_39':
                AgeRange=3
            elif tmp.AgeRange[i]=='Age_40_49':
                AgeRange=4
            elif tmp.AgeRange[i]=='Age_50_59':
                AgeRange=5
            elif tmp.AgeRange[i]=='Age_60_69':
                AgeRange=6
            elif tmp.AgeRange[i]=='Age_70_plus':
                AgeRange=7
            if tmp.Class_[i]=='Class1':
                Class_=0
            elif tmp.Class_[i]=='Class2':
                Class_=1
            elif tmp.Class_[i]=='Class3':
                Class_=2
            if tmp.Embarked_[i]=='Southampton':
                Embarked_=0
            elif tmp.Embarked_[i]=='Cherbourg':
                Embarked_=1
            elif tmp.Embarked_[i]=='Queenstown':
                Embarked_=2
            elif tmp.Embarked_[i]=='Southampton':
                Embarked_=3
            dt.append([Sex,AgeRange,Class_,tmp.SiblingSpouse[i],tmp.ParentChild[i],Embarked_,tmp.Survived[i]])
    elif k==2:# dataset_for_MultiLinear_regression
        for i in range(len(tmp.Age)):
            dt.append([tmp.Age[i],tmp.Weight[i],tmp.Height[i],
            tmp.Neck[i],tmp.Chest[i],tmp.Abdomen[i],tmp.Hip[i],
            tmp.Thigh[i],tmp.Knee[i],tmp.Ankle[i],tmp.Biceps[i],
            tmp.Forearm[i],tmp.Wrist[i],tmp.FAT_PER[i]])
    elif k==3:# dataset_for_PCA_LDA
        TEST_RESULT=0
        for i in range(len(tmp.LOC_BLANK)):
            if tmp.TEST_RESULT[i]=='FAIL':
                TEST_RESULT=0
            elif tmp.TEST_RESULT[i]=='PASS':
                TEST_RESULT=1
            dt.append([
            tmp.LOC_BLANK[i],	tmp.BRANCH_COUNT[i],tmp.CALL_PAIRS[i],tmp.LOC_CODE_AND_COMMENT[i],
            tmp.LOC_COMMENTS[i],tmp.CONDITION_COUNT[i],tmp.CYCLOMATIC_COMPLEXITY[i],
            tmp.CYCLOMATIC_DENSITY[i],tmp.DECISION_COUNT[i],tmp.DECISION_DENSITY[i],
            tmp.DESIGN_COMPLEXITY[i],tmp.DESIGN_DENSITY[i],tmp.EDGE_COUNT[i],tmp.ESSENTIAL_COMPLEXITY[i]
            ,tmp.ESSENTIAL_DENSITY[i],tmp.LOC_EXECUTABLE[i]
            ,tmp.PARAMETER_COUNT[i],tmp.GLOBAL_DATA_COMPLEXITY[i],tmp.GLOBAL_DATA_DENSITY[i]
            ,tmp.HALSTEAD_CONTENT[i],tmp.HALSTEAD_DIFFICULTY[i],tmp.HALSTEAD_EFFORT[i],
            tmp.HALSTEAD_ERROR_EST[i],tmp.HALSTEAD_LENGTH[i],tmp.HALSTEAD_LEVEL[i],
            tmp.HALSTEAD_PROG_TIME[i],tmp.HALSTEAD_VOLUME[i],tmp.MAINTENANCE_SEVERITY[i],
            tmp.MODIFIED_CONDITION_COUNT[i],tmp.MULTIPLE_CONDITION_COUNT[i],tmp.FAILDE_COUNT[i],
            tmp.FAILRMALIZED_CYLOMATIC_COMPLEXITY[i],tmp.NUM_OPERANDS[i],tmp.NUM_OPERATORS[i],
            tmp.NUM_UNIQUE_OPERANDS[i],tmp.NUM_UNIQUE_OPERATORS[i],tmp.NUMBER_OF_LINES[i],
            tmp.PERCENT_COMMENTS[i],tmp.LOC_TOTAL[i],TEST_RESULT
            ])
    elif k==4:# dataset_for_Poly_regression
        for i in range(len(tmp.Rating)):
            dt.append([tmp.Rating[i],tmp.Reviews[i],chuyenDoiDuLieu(tmp.Size[i]),locKyTu(tmp.Installs[i])])
    return dt
