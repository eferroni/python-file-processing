import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('CRITICAL')
logger.error('ERROR')
logger.warning('WARNING')
logger.info('INFO')
logger.debug('DEBUG')