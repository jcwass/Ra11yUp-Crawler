import sys
import crawler
import validator

starter = crawler.Crawler()
new_validator = validator.Validator()

url = sys.argv[1]
check_robots = sys.argv[2]
if new_validator.does_url_exist(url):
    finished = starter.start_crawls(url, check_robots)
else:
    print(f"{url} is not a valid url.")