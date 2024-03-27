import logging

def init_logging(module_name, log_file_path):
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(module_name)

    logger.addHandler(file_handler)

    return logger

