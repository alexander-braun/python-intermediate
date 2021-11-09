import logging

# EXAMPLE WITH CONFIG
# import logging.config
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')


# EXAMPLE WITHOUT CONFIG
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# set level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# specify formatters
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

# run -> 
# stream-handler loggs messages of level warning and above
# file-handler logs messages of level error and above