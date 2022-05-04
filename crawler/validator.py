import requests

class Validator():
    '''Handles all validation for various crawl elements.
        Stereotype:
            Information Holder
        Attributes:
            self.crawled_list (List): A list of all urls already crawled.
            self.in_file (List): A list of all items already tracked in the entry_point file.
    '''

    # Initializes the classes attributes.
    def __init__(self):
        self.crawled_list = []
        self.in_file = []
    
    # Checks to see if a provided url exists
    def does_url_exist(self, url):
        try:
            url_request = requests.head(url)
            if url_request.status_code < 400:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(e)

    # Appends a url to the crawled_list attribute.
    def add_to_crawled(self, url):
        self.crawled_list.append(url)

    # Checks to see if the url provided has been crawled or not.
    def has_crawled(self, url):
        if url in self.crawled_list:
            return True
        else:
            return False

    # Appends a url to the in_file attribute.
    def add_to_file_list(self, url):
        self.in_file.append(url)

    # Checks to see if the provided url exists in the in_file list.
    def has_added_to_entry(self, url):
        if url in self.in_file:
            return True
        else:
            return False