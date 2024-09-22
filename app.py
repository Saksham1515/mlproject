from src.ml_Project.logger import logging
from src.ml_Project.exception import CustomException
from src.ml_Project.components.model_trainer import ModelTrainer
from src.ml_Project.components.data_ingestion import DataIngestion
from src.ml_Project.components.data_transformation import DataTransformation
import sys
import mlflow
import dagshub
dagshub.init(repo_owner='Saksham1515', repo_name='mlproject', mlflow=True)

if __name__ == "__main__":
    logging.info("The execution is started~")

    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)
        
        model_trainer =  ModelTrainer()
        r2_score_value = model_trainer.initiate_model_trainer(train_arr,test_arr)
        print(r2_score_value)
    
    except Exception as e:
        logging.info("Custom Execption")
        raise CustomException(e,sys)
    
    mlflow.set_tracking_uri(uri="https://dagshub.com/Saksham1515/mlproject.mlflow")