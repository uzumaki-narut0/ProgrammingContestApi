import urllib2
import json
from dateutil.parser import parse
from datetime import datetime

def scrape(resultSet):
    url = "https://www.hackerearth.com/chrome-extension/events/"
    page = urllib2.urlopen(url)
    data = json.load(page)
    allevents = data["response"]
    for event in allevents:
        if(event["status"] == "UPCOMING"):
            code = event["challenge_type"]
            name = event["title"]
            start_time = parse(event["start_timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            end_time = parse(event["end_timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            platform = "hackerearth"
            contest_url = event["url"]
            resultSet["upcoming_contests"].append({"code":code,"platform":platform,"name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})
        else:
            code = event["challenge_type"]
            name = event["title"]
            start_time = parse(event["start_timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            end_time = parse(event["end_timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            platform = "hackerearth"
            contest_url = event["url"]
            resultSet["present_contests"].append({"code":code,"platform":platform,"name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})

if __name__ == '__main__':
    scrape()