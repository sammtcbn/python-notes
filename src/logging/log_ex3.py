import os
import logging

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

def main():
    log_init()

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical error message')

if __name__ == '__main__':
    main()
