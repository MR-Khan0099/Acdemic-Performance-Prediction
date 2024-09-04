# import os
# import sys
# import numpy as np
# import pandas as pd
# import dill
# from sklearn.metrics import r2_score
# from src.exception import CustomException
# from src.logger import logging



# def save_object(obj, file_path):
#     try:
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)

#         with open(file_path, "wb") as file_obj:
#             dill.dump(obj, file_obj) #dill library is used to make pkl file

#     except Exception as e:
#         raise CustomException(e, sys)
    
# def evaluate_models(models, x_train,y_train, x_test, y_test):
#     report={}
#     try:
#         for i in range(len(list(models))):
#             model = list(models.values())[i]

#             model.fit(x_train, y_train)

#             y_train_pred = model.predict(x_train)

#             y_test_pred = model.predict(x_test)

#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)

#             report.list(models.keys())[i] = {"train_score":train_model_score, "test_score":test_model_score}
           
        
#     except Exception as e:
#         logging.error("Error occurred while evaluating the model: ", e)
#         raise CustomException(e, sys)

import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging

def save_object(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)  # dill library is used to make pkl file

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(models, x_train, y_train, x_test, y_test):
    report = {}
    try:
        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(x_train, y_train)

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Correct assignment to the report dictionary
            model_name = list(models.keys())[i]
            report[model_name] = {"train_score": train_model_score, "test_score": test_model_score}
        
    except Exception as e:
        logging.error("Error occurred while evaluating the model: ", e)
        raise CustomException(e, sys)

    return report
