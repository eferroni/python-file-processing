import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.WARNING)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('My CRITICAL message')
logger.error('My ERROR message')
logger.warning('My WARNING message')
logger.info('My INFO message')
logger.debug('My DEBUG message')
