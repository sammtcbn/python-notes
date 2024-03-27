from log_ex2_lib import (
    init_logging
)

from log_ex2_func import (
    myfunc
)

def test1():
    myfunc("test1")

def test2():
    modulename = "log_ex2"
    logfile    = "log_ex2.log"

    logger = init_logging(modulename, logfile)

    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')

    myfunc("test2", logger)

def main():
    test1()
    test2()

if __name__ == '__main__':
    main()
