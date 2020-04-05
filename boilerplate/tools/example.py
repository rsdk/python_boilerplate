import time
import logging
from boilerplate.timer import Timer

logger = logging.getLogger(__name__)

print(__name__)
@Timer(name='sleeper', text='sleeper executed in {:.3f} seconds', logger=logger.info)
def sleeper(t_sec=1):
    logger.debug(f'sleeping for {t_sec} seconds')
    time.sleep(t_sec)
    return t_sec
