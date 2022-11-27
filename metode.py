import joblib
import pandas as pd

# preprocessing
def normalisasi(x):
    # import data test
    cols = ['age','sex','BP','cholestrol']
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('model/data_test2.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(other=df,ignore_index=True)
    # return data_test yang sudah dinormalisasi
    return joblib.load('model/norm.sav').fit_transform(data_test)

# normal
def normal(x):
    cols = ['age','sex','BP','cholestrol']
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('model/data_test2.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(other=df,ignore_index=True)
    # return data_test yang sudah dinormalisasi
    return (data_test)

# metode with normalization
def knn(x):
    
    return joblib.load('model/modelKNN11.pkl').predict(x)

def bagging(x):
    return joblib.load('model/bagginggaussian.pkl').predict(x)

def randomforest(x):
    return joblib.load('model/randomforest.pkl').predict(x)

# metode without normalization
def knn_no_norm(x):
    return joblib.load('model/modelKNN11_1.pkl').predict(x)

def bagging_no_norm(x):
    return joblib.load('model/bagginggaussian_1.pkl').predict(x)

def randomforest_no_norm(x):
    return joblib.load('model/randomforest_1.pkl').predict(x)


# print(normalisasi([50,1,120,200]))