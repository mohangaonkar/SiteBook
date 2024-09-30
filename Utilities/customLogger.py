import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = "./Logs"  # Ensure no extra quotes are present
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format='%(asctime)s: %(levelname)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO  # Ensure the level is set to INFO or lower
        )
        logger = logging.getLogger()
        return logger

