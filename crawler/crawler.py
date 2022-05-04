from urllib.parse import urlparse
import urllib.robotparser as urobot
import logging
import getpass
import time
from datetime import datetime
from crawler.validator import Validator
from crawler.crawl import Crawl
from crawler.file_crawl import File_Crawl

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

    # Start the crawl process.
    def start_crawls(self):

        # Asks for the url to be crawled, then checks to ensure it is valid.
        # Valid url: 'https://ra11yup.linearbsystems.net'
        self.url = input("Please type a full URL to crawl: ")
        valid_url = self.validator.does_url_exist(self.base_url)
        while valid_url == False:
            self.url = input("Invalid URL, please try again: ")
            valid_url = self.validator.does_url_exist(self.base_url)

        # Runs the create base function.
        self.create_base()

        # These lines define date and other relevent info for logging purposes.
        d = datetime.today()
        epoch_time = time.mktime(d.timetuple())
        logging.basicConfig(filename=f'logs/crawl-{getpass.getuser()}.{epoch_time}.log', level=logging.DEBUG )

        # Checks to see if a robots.txt file exists and initializes a robots parser.
        rp = urobot.RobotFileParser()
        rp.set_url(self.base_url + "/robots.txt")
        rp.read()
        robots = self.base_url + '/robots.txt'

        # Clearing the entry_point file.
        f = open('res/crawl-entry-point.txt', 'w')
        f.close()
        has_robots = self.validator.does_url_exist(robots)

        # Begins the initial crawl and then calls the file_crawl object.
        initial_crawl = Crawl(self.url, has_robots, rp, self.base_url, self.validator)
        initial_crawl.get_all_url()
        self.validator.add_to_crawled(self.url)
        file_crawl = File_Crawl(self.validator, self.base_url)
        file_crawl.file_entry_point_crawl()

    # Creates a base url for the crawl.
    def create_base(self): 
        parsed_url = urlparse(self.url)
        parsed_scheme = parsed_url.scheme + "://"
        self.base_url = parsed_scheme + parsed_url.netloc
