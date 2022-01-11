import pickle
import json
import numpy as np 

__data_columns = None
__model = None

def predict_disease(Age,ALB,ALP,ALT,AST,BIL,CHE,CHOL,CREA,GGT,PROT,Sex):

    x = np.zeros(shape= (1,13))
    
    if Sex=='m' or Sex == 'M' or Sex== 'Male':
        Sex_m = 1
        Sex_f = 0
    else:
        Sex_m = 0
        Sex_f = 1
        
    x[0] = [Age,ALB,ALP,ALT,AST,BIL,CHE,CHOL,CREA,GGT,PROT,Sex_f, Sex_m]
    predicted = __model.predict(x)[0]

    if predicted==1:
        return "Hepatitis"
    elif predicted==2:
        return "Fibrosis"
    elif predicted==3:
        return "Cirrhosis"
    else:
        return "Healthy"


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/Hepatitis_predict.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(predict_disease(32,38.5,52.5,7.7,22.1,7.5,6.93,3.23,106.0,12.1,69.0,'f'))
    print(predict_disease(30,37,60.2,10,80,12,600.07,5.3,67,34,68,'f'))
