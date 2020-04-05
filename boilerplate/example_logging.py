import json
import logging
from logging.config import dictConfig

with open('../logging_conf.json') as fp:
    logging_conf = json.load(fp)

dictConfig(logging_conf)
logger = logging.getLogger()
logger.debug('test')
