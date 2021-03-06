import sys
import time
import urllib.request
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

class Crawl():
    '''This class handles each crawl instance and writes data to the various locations
    to track crawl.
        Stereotype:
            Information Holder
        Attributes:
            self.url (String): a url string.
            self.has_robots (Boolean): Indicates whether or not the url has a robots.txt file.
            self.rp (urobot.RobotFileParser()): Instance of the urobot.RobotFileParser() object.
            self.base_url (String): A string of the base url of the site.
            self.validator (Validator): An instance of the Validator object.
    '''

    # Initializes the class variables.
    def __init__ (self, url, has_robots, base_url, validator, robot_parser, logger):
        self.url = url
        self.path = urlparse(self.url).path
        self.has_robots = has_robots
        self.base_url = base_url
        self.validator = validator
        self.robot_parser = robot_parser
        self.logger = logger

    def flush_then_wait(self):
        sys.stdout.flush()
        sys.stderr.flush()
        time.sleep(0.5)
    
    def get_all_url(self):
    # Loops through a web page and grabs all urls found on the page.
        if (self.robot_parser.check_url(self.path) or not self.has_robots):


            url_list = []

            # Get the input url web page HTML content.
            html_data = urllib.request.urlopen(self.url).read().decode("utf-8")

            # Create an instance of BeautifulSoup with the above HTML data.
            soup = BeautifulSoup(html_data, features='html.parser')

            # Get all HTML a tag on the web page in a list.
            tag_list = soup.find_all('a')

            # Loop the above tag list.
            for tag in tag_list:

                # Get the HTML a tag href attribute value.
                href_value = str(tag.get('href'))
                if not 'http' in href_value:
                    href_value = urljoin(self.base_url, href_value)

                if href_value.split('#') not in url_list:
                    url_list.append(href_value)

            # Removing duplicate values from the url list.
            final_url_list = set(url_list)
            
            # Looping through the url list and adding url to crawl entry.
            for url in final_url_list:
                if url[-1] != '/' and '.html' not in url and '.php' not in url:
                    url = url + '/'
                if (self.robot_parser.check_url(urlparse(url).path) or not self.has_robots) and self.validator.check_pinged(url) and 'mailto' not in url:
                    page = requests.head(url)
                    f = open('Ra11yUp-Crawler/res/crawl-entry-point.txt', 'a+')
                    if page.status_code < 400 and not self.validator.has_added_to_entry(url) and self.base_url[:-1] in url:
                        f.write(f'{url}\n')

                        # Adds the url to the list of crawled urls.
                        self.validator.add_to_file_list(url)
                    
                    # Logs all urls to a log file.
                    self.validator.add_to_pinged(url)
                    self.logger.write(url,page.status_code)

                    f.close()
        else:
            print("Can't scrape.")