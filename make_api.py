from time import strptime
import codechef_scraper
import codeforces_scraper
import hackerearth_scraper

def make_api(resultSet):
	codeforces_scraper.scrape(resultSet)
	codechef_scraper.scrape(resultSet)
	hackerearth_scraper.scrape(resultSet)
	resultSet["upcoming_contests"] = sorted(resultSet["upcoming_contests"], key=lambda k: strptime(k['start_time'], "%Y-%m-%d %H:%M:%S"))
	resultSet["present_contests"] = sorted(resultSet["present_contests"], key=lambda k: strptime(k['start_time'], "%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    make_api()
