import logging
from random import randint

FORMAT = '%(levelname)s - %(message)s'

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

for count in range(60):
    temp = randint(0, 46)
    if temp < 30:
        logger.debug(f"{temp} C")
    elif temp > 35:
        logger.critical(f"{temp} C")
    else:
        logger.warning(f"{temp} C")
