import logging

# by default only WARNING, ERROR and CRITICAL are printed to the console -> changed by this:
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# log to 5 different log levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


import logging_helper

# capturing stack traces
try:
  a = [1, 2, 3]
  val = a[4]
except IndexError as e:
  # include the stacktrace with exc_info
  logging.error(e, exc_info=True)

# same thing with traceback
import traceback
try:
  a = [1, 2, 3]
  val = a[4]
except:
  logging.error("The error is %s", traceback.format_exc())


# rotating file-handlers
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
  # roll over after 2KB and keep backup logs app.log.1, app.log.2, etc...
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
  logger.info('Hello world!')
