import sys
from urllib.parse import urlparse
from robots_parser import Robots_Parser
import logging
import getpass
import time
from datetime import datetime
from validator import Validator
from crawl import Crawl
from file_crawl import File_Crawl

class Crawler ():
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
        self.base_url = ""
        self.url = ""
        self.validator = Validator()
        self.robots_parser = ''

    # Start the crawl process.
    def start_crawls(self, url, check_robots):

        # Asks for the url to be crawled, then checks to ensure it is valid.
        # Valid url: 'https://ra11yup.linearbsystems.net'
        self.url = url

        # Runs the create base function.
        self.create_base()

        # These lines define date and other relevant info for logging purposes.
        d = datetime.today()
        epoch_time = time.mktime(d.timetuple())
        logging.basicConfig(filename=f'Ra11yUp-Crawler/logs/crawl-{getpass.getuser()}.{epoch_time}.log', level=logging.DEBUG )

        # Creating Robot Parser
        robots = self.base_url + '/robots.txt'
        self.robots_parser = Robots_Parser(robots)

        # Clearing the entry_point file.
        f = open('Ra11yUp-Crawler/res/crawl-entry-point.txt', 'w')
        f.close()
        if check_robots:
            has_robots = self.validator.does_url_exist(robots)
        else: 
            has_robots = False

        # Begins the initial crawl and then calls the file_crawl object.
        sys.stdout.write(f'Crawling: {self.url}')
        initial_crawl = Crawl(self.url, has_robots, self.base_url, self.validator, self.robots_parser)
        initial_crawl.get_all_url()
        self.validator.add_to_crawled(self.url)
        file_crawl = File_Crawl(self.validator, self.base_url, check_robots, self.robots_parser)
        file_crawl.file_entry_point_crawl()

    # Creates a base url for the crawl.
    def create_base(self): 
        parsed_url = urlparse(self.url)
        parsed_scheme = parsed_url.scheme + "://"
        self.base_url = parsed_scheme + parsed_url.netloc
