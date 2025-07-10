import sys
import logging

def error_message_detail(error,error_detail:sys):
    """
    Returns a detailed error message.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] line number: [{exc_tb.tb_lineno}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that formats error messages.
    """
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1 / 0  # This will raise a ZeroDivisionError
#     except Exception as e:
#         logging.info("An error occurred")
#         raise CustomException(e, sys)
#     # This will print the detailed error message when run directly
#     # You can also test this by importing this module in another script