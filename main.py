#why create "__init__.py" inside the src/cnnClassifier folder
# because when we will call the method like logger, then don't need to call like "src.cnnClassifier" 
# just call cnnClassifier import logger
#Example:
from src.cnnClassifier import logger


logger.info("Welcome to our custom log")