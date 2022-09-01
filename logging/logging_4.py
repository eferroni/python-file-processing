import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(level=logging.ERROR, filename='prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger()
logger.critical('My CRITICAL message')
logger.error('My ERROR message')
logger.warning('My WARNING message')
logger.info('My INFO message')
logger.debug('My DEBUG message')
