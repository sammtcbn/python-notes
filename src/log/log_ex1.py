import logging

# Set logging level
logging.basicConfig(level=logging.DEBUG)

# Set the log file name and level
file_handler = logging.FileHandler('log_ex1.log')
file_handler.setLevel(logging.WARNING)

# Set the log record format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the FileHandler to the root logger
logger = logging.getLogger()
logger.addHandler(file_handler)

# Write log records
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical error message')
