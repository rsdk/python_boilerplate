import time
import logging
from boilerplate.timer import Timer

logger = logging.getLogger(__name__)

print(__name__)


@Timer(name='sleeper', text='sleeper executed in {:.3f} seconds', logger=logger.info)
def sleeper(t_sec=1):
    """
    Function to let a specific time pass.

    :param t_sec:
    :return: t_sec

    >>> sleeper(1)
    1
    >>> sleeper(0.5)
    0.4
    """
    logger.debug(f'sleeping for {t_sec} seconds')
    time.sleep(t_sec)
    return t_sec


if __name__ == '__main__':
    import doctest

    doctest.testmod()
