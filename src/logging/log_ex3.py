import os
import logging
import time

def log_init():
    logfilename = os.path.join(os.getcwd(), os.path.basename(__file__).split('.')[0]+'.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s: %(message)s",
        handlers=[
            logging.FileHandler(logfilename),
            logging.StreamHandler()
        ]
    )

def log_level_set(level):
    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

def main():
    log_init()

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical error message')

    time.sleep(3)

    log_level_set(logging.WARNING)

    logging.debug('This is a debug message')      # This won't be displayed
    logging.info('This is an info message')       # This won't be displayed
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical error message')

if __name__ == '__main__':
    main()
