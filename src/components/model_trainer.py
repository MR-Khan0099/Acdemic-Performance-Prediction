import os
import sys
import logging
from dataclasses import dataclass
from src.exception import CustomException

from catboost import CatBoostRegressor

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBClassifier, XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_models, save_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_array, test_array):

        try:
            logging.info("Splitting the data into train and test arrays")
            x_train,y_train,x_test,y_test = (train_array[::-1],#take out last and feed it to the model
                                             train_array[:,-1],#
                                             test_array[::-1],
                                             test_array[:,-1]
            )
            
            models = {
                "RandomForest": RandomForestRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "AdaBoost classifier": AdaBoostRegressor(),
                "XGBoost": XGBRegressor(),
                "CatBoost": CatBoostRegressor(verbose=False),
                "DecisionTree": DecisionTreeRegressor(),
                "LinearRegression": LinearRegression(),
                "k-Neighbors": KNeighborsRegressor(),
                "XGBClassifier": XGBClassifier(),
            }

            model_report:dict= evaluate_models(x_train=x_train, y_train=y_train,x_test=x_test, y_test=y_test, 
                                              models=models)
            
            # get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.7:
                raise CustomException("No best model found", sys)


            logging.info(f"Best found model on the basis of R2 score is: {best_model_name}")        

        
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predictions = best_model.predict(x_test)

            r2_score = r2_score(y_test, predictions)
            return r2_score

           
        except Exception as e:
            raise CustomException(e, sys)




