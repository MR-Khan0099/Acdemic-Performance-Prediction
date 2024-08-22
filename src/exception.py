import sys
import logging
import os


def error_message_detail(error, error_detail):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exec_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        _,_,exec_tb = error_detail.exc_info()
        super().__init__(error_message_detail(error_message, error_detail))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    


# Global exception handler
def global_exception_handler(type, value, traceback):
    logging.error("Uncaught exception:", exc_info=(type, value, traceback))

# Set the global exception hook
sys.excepthook = global_exception_handler

# Example usage within the exception handler script
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)




