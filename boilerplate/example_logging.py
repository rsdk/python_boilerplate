import json
import logging
from logging.config import dictConfig
import boilerplate.tools.example

with open('../logging_conf.json') as fp:
    logging_conf = json.load(fp)
dictConfig(logging_conf)
logger = logging.getLogger()

if __name__ == '__main__':
    logger.debug('test')
    ret = boilerplate.tools.example.sleeper(0.03)
    print(ret)
