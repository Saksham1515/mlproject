import logging
import os 
import datetime

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S_")}".log
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

Log_file_path = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename = Log_file_path,
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s',
    level=logging.INFO,   
)