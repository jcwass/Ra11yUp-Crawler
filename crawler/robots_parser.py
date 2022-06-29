import os

class Robots_Parser:

    def __init__ (self, url, base_url):
        self.url = url
        self.robots = base_url + '/robots.txt'
        self.base_url = base_url
        self.result_data_set = None
        self.get_results(self.robots)

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
    
    def check_url(self, url):
        for item in self.result_data_set.get('Disallowed'):
            if item in url:
                return False
        return True