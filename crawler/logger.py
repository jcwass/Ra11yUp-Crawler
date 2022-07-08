import logging
import time
from datetime import datetime


class Logger ():
    '''Crawls the entry_point file provided by the initial crawl.
    Stereotype:
        Controller
    Attributes:
        self.base_url (String): A string of the base url of the site.
        self.url (String): a url string.
        self.validator (Validator()): An instance of the Validator object.
    '''

    # Initializes class attributes.
    def __init__(self):
        self.d = datetime.today()
        self.epoch_time = time.mktime(self.d.timetuple())
        self.oneXX_logger = self.setup_logger('100 level logger', f'Ra11yUp-Crawler/logs/crawl-1XX-{self.epoch_time}.log')
        self.twoXX_logger = self.setup_logger('200 level logger', f'Ra11yUp-Crawler/logs/crawl-2XX-{self.epoch_time}.log' )
        self.threeXX_logger = self.setup_logger('300 level logger', f'Ra11yUp-Crawler/logs/crawl-3XX-{self.epoch_time}.log')
        self.fourXX_logger = self.setup_logger('400 level logger', f'Ra11yUp-Crawler/logs/crawl-4XX-{self.epoch_time}.log')
        self.fiveXX_logger = self.setup_logger('500 level logger', f'Ra11yUp-Crawler/logs/crawl-5XX-{self.epoch_time}.log')

    def setup_logger(self, logger_name, log_file, level=logging.INFO):

        log_setup = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler(log_file, mode='a')
        streamHandler = logging.StreamHandler()
        log_setup.setLevel(level)
        log_setup.addHandler(fileHandler)
        log_setup.addHandler(streamHandler)



    def write(self, url, status_code):
        if str(status_code)[:1] == '2':
            log = logging.getLogger('200 level logger')
            log.info('Page status for {} is: {}'.format(url,status_code))
        elif str(status_code)[:1] == '4':
            log = logging.getLogger('400 level logger')
            log.info('Page status for {} is: {}'.format(url,status_code))
        elif str(status_code)[:1] == '5':
            log = logging.getLogger('500 level logger')
            log.info('Page status for {} is: {}'.format(url,status_code))
        elif str(status_code)[:1] == '3':
            log = logging.getLogger('300 level logger')
            log.info('Page status for {} is: {}'.format(url,status_code))
        else:
            log = logging.getLogger('100 level logger')
            log.info('Page status for {} is: {}'.format(url,status_code))