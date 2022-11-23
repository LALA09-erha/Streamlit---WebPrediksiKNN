import joblib
import pandas as pd

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

def knn(x):
    
    return joblib.load('model/modelKNN11.pkl').predict(x)


# print(normalisasi([50,1,120,200]))