import logging

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')

logger = logging.getLogger()
logger.critical('CRITICAL message')
logger.error('ERROR message')
logger.warning('WARNING message')
logger.info('INFO message')
logger.debug('DEBUG message')