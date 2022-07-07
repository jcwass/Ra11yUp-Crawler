import sys
from crawl import Crawl

class File_Crawl():
    '''Crawls the entry_point file provided by the initial crawl.
        Stereotype:
            Information Holder
        Attributes:
            self.entry_point (String): The location of the entry point txt file.
            self.validator (Validator()): An instance of the Validator object.
            self.base_url (String): A string of the base url of the site.
    '''
    # Initializes class attributes.
    def __init__(self, validator, base_url, check_robots, robot_parser):
        self.entry_point= "Ra11yUp-Crawler/res/crawl-entry-point.txt"
        self.validator = validator
        self.base_url = base_url
        self.check_robots = check_robots
        self.robot_parser = robot_parser

    # Initializes a crawl instance for each url that has not been crawled.
    def file_entry_point_crawl(self):
        
        # Loops through entry point file and creates a list out of each line.
        with open(self.entry_point) as fh:
            urls = fh.readlines()

        # Looping through each url in the list defined above.
        for url in urls:
            url = url.strip()

            # Checks to see if the url has been crawled.
            if not self.validator.has_crawled(url):
                robots = self.base_url + '/robots.txt'
                if self.check_robots:
                    has_robots = self.validator.does_url_exist(robots)
                else: 
                    has_robots = False
                sys.stdout.write(f'\nCrawling: {url}')
                new_crawl = Crawl(url, has_robots, self.base_url, self.validator, self.robot_parser)
                new_crawl.get_all_url()
                self.validator.add_to_crawled(url)