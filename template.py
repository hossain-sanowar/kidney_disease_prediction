import os
from pathlib import Path
import logging

#logging string
#to create the end to end project, log statement is very important for the project
#that's why I use this logging file to store the execution statement after each and every ststement.

#create the information related log and specific format of the log 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:%(levelname)s:')

#Create the project name
project_name='cnnClassifier'

#Create list of files and folder for the structure
#just, I am follow the Keras structure. here I am using "src" instead of "Keras"
#https://github.com/keras-team/keras/tree/master/keras
list_of_files = [
    ".github/workflows/.gitkeep", #if folder is empty then github won't update because of .gitkeep
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    'test.py'

]

for filepath in list_of_files:
    filepath = Path(filepath) # Path is used for any kind of operating system and convert it for like Windows, mac and linux;
    filedir, filename = os.path.split(filepath)#separate folder path and file path like folder_path: src/{project_name}/components/, file_path: __init__.py


    if filedir !="": #folder is already present, it won't be created
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}") #message infor fo creating the folder

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #not exist filepath or file size is zero, then create it
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}") #message info for creating the file


    else:
        logging.info(f"{filename} is already exists") #alreday exist folder and file, then create this message.
