import urllib.robotparser as urobot
from crawler.crawl import Crawl

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
    def __init__(self, validator, base_url):
        self.entry_point= "res/crawl-entry-point.txt"
        self.validator = validator
        self.base_url = base_url

    # Loops through each url found in the entry_point.txt file. 
    # Initializes a crawl instance for each url that has not been crawled.
    def file_entry_point_crawl(self):
        
        # Loops through entry point file and creates a list out of each line.
        with open(self.entry_point) as fh:
            urls = fh.readlines()

        # Looping through each url in the list defined above.
        for url in urls:
            url = url.strip()

            # Checks to see if the url has been crawled.
            if self.validator.has_crawled(url):
                rp = urobot.RobotFileParser()
                rp.set_url(url + "/robots.txt")
                rp.read()
                robots = url + '/robots.txt'
                has_robots = self.validator.does_url_exist(url)
                new_crawl = Crawl(url, has_robots, rp, self.base_url, self.validator)
                new_crawl.get_all_url()
                self.validator.add_to_crawled(url)