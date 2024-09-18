from src.ml_Project.logger import logging
from src.ml_Project.exception import CustomException
from src.ml_Project.components.data_ingestion import DataIngestion
from src.ml_Project.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("The execution is started~")

    try:
        # data_ingestion_config = DataIngestionConfig() 
        data_ingestion = DataIngestion()
        data_ingestion.initate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Execption")
        raise CustomException(e,sys)