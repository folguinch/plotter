import os, logging
import logging.handlers

def get_level(args):
    numeric_level = getattr(logging, args.loglevel[0].upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.loglevel[0])
    return numeric_level

def get_logger(name, args, file_name='plotter.log'):
    """Creates a new logger.

    Parameters:
        name (str): name of the logger.
        file_name (str): file name of the log.
    Keywords:
        filelevel (default=logging.DEBUG): logging to file level.
        stdoutlevel (default=logging.INFO): logging to std output level.
        filefmt (str, default=%(asctime)s - %(name)s - %(levelname)s: %(message)s): 
            logging to file message format.
        stdoutfmt (str, default=%(levelname)s: %(message)s): 
            logging to std output message format.
        maxBytes (int, default=5MB): maximum size of logging file in bytes.
        backupCount (int, default=5): maximum number of log files to rotate.
    """
    # Create logger
    logger = logging.getLogger(name)
    if not len(logger.handlers):
        logger.setLevel(logging.DEBUG)

        # File handler
        file_name = os.path.expanduser(file_name)
        filefmt = '%(asctime)s [%(levelname)s] - %(filename)s '+\
                '(%(funcName)s:%(lineno)s): %(message)s'
        fh = logging.handlers.RotatingFileHandler(file_name,
                maxBytes=5242880, backupCount=5)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter(filefmt))

        # Stream handler
        sh = logging.StreamHandler()
        sh.setLevel(get_level(args))
        if args.loglevel[0].lower()=='debug':
            streamfmt = '%(levelname)s - %(filename)s (%(funcName)s): %(message)s'
        else:
            streamfmt = '%(levelname)s: %(message)s'
        sh.setFormatter(logging.Formatter(streamfmt))

        # Register handlers
        logger.addHandler(fh)
        logger.addHandler(sh)

    args.logger = logger

def logger_from_config(file_name):
   pass 
