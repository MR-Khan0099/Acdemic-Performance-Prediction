
# import logging
# import os
# from datetime import datetime  # corrected import statement

# # Create a logs directory if it doesn't exist
# logs_path = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_path, exist_ok=True)

# # Create a log file with the current timestamp
# LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"  # corrected file name format
# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# # Set up basic logging configuration
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     level=logging.INFO,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # added missing format attributes
# )



# #for checking 
# if __name__ == "__main__":
#     logging.info("Logging has started.")
    
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
