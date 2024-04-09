def myfunc(msg, logger=None):
    if logger:
        print("have logger")
        logger.info(msg)
        logger.warn(msg)
        logger.error(msg)
    else:
        print("no logger")
