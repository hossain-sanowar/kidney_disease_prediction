#main benefit for logger here because if we can execute any command
# and call the logger folder, no need to call src.cnnClassifer, just we can call cnnClassifer
# we can create this log file to other folder

import os
import sys
import logging #python inbuilt function. we can create custom log file
 

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
#asctime: is store the asc time that's mean current time;
#levelname: is the log level name; information level log
#module: is the module name; which module is running this like template.py, dataingestion.py
#message: print the message like from where getting the error message

log_dr="logs" #create a log folder
os.makedirs(log_dr, exist_ok=True) #check folder exist or not
log_filepath=os.path.join(log_dr, "running_logs.log") #log file


logging.basicConfig(
    level=logging.INFO, #log level name
    format=logging_str, #log format as string; define function above 
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #print inside the terminal
    ]
)

logger=logging.getLogger("cnnClassifierLogger") #create logger object and return to main.py file