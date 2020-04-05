import requests
import datetime
import os.path
import logging
from boilerplate.timer import Timer

logger = logging.getLogger(__name__)


@Timer(name='dl_covid_stats', text='dl_covid_stats executed in {:.3f} seconds', logger=logger.info)
def dl_covid_stats():
    """
    Download daily csv with covid statistics if not downladed today.

    :return:
    """
    dt_str = datetime.date.today().isoformat()
    filename = f'stats_{dt_str}.csv'
    if os.path.isfile(filename):
        logging.info(f"current file already downloaded: {filename}")
    else:
        url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        logging.info(f"downloaded and saved file: {filename}")

