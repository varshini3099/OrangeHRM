import logging
import os

class LogGen:

    @staticmethod
    def logger():
        log_dir = "../Logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'automation.log')
        logger = logging.getLogger("customlogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger


