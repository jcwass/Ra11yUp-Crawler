import os

class Robots_Parser:
    '''Parses robots.txt file. Contains methods for checking if a url can be crawled according
    to robots.txt.
        Stereotype:
            Information Holder
        Attributes:
            self.robots (string): The URL location of the robots.txt file.
            self.result_data_set (Dictionary): A dictionary containing two sublist, one for Allowed and Disallowed urls.
    '''

    # Initializes the class variables.
    def __init__ (self, robots):
        self.robots = robots
        self.result_data_set = {}
        self.get_results(self.robots)

    # Parses the robots.txt file and fill the result_data_set dictionary.
    def get_results(self, url):
        result = os.popen(f"curl {url}").read()
        result_data_set = {"Disallowed":[], "Allowed":[]}
        for line in result.split("\n"):
            if line.startswith('User-agent'):
                current_agent = line.split(': ')[1].split(' ')[0]
            if current_agent == '*':
                if line.startswith('Allow'):    # this is for allowed url
                    result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info
                elif line.startswith('Disallow'):    # this is for disallowed url
                    result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info
        self.result_data_set = result_data_set
    
    # Determines if the URL path presented can be crawled.
    def check_url(self, url):
        for item in self.result_data_set.get('Disallowed'):
            if item in url:
                for allowed in self.result_data_set.get('Allowed'):
                    if allowed == url:
                        return True
                return False
        return True