# help in debugging, error handling, and logging
# check till where the code is running
# project traacking, helps after deployment, no need to open console or code to check the errors
import logging
import os
import sys
from datetime import datetime 

log_file = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs", log_file)
os.makedirs(logs_dir, exist_ok=True)
log_file_path = os.path.join(logs_dir, log_file)


logging.basicConfig(
    filename= log_file_path ,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,       # 5 levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    
)