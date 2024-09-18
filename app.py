from src.ml_Project.logger import logging
from src.ml_Project.exception import CustomException
from src.ml_Project.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.ml_Project.components.data_transformation import DataTransformationConfig , DataTransformation
import sys

if __name__ == "__main__":
    logging.info("The execution is started~")

    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)
        
    except Exception as e:
        logging.info("Custom Execption")
        raise CustomException(e,sys)