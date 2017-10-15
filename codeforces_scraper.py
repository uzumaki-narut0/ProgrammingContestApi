import urllib2
import json
from dateutil.parser import parse
from datetime import datetime

def scrape(resultSet):
    def posix_to_normal(time):
        return datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
    url = 'http://codeforces.com/api/contest.list'
    page = urllib2.urlopen(url)
    data = json.load(page)
    allevents = data["result"]
    for event in allevents:
        if(event["phase"] == "FINISHED"):
            break
        if(event["phase"] == "BEFORE"):
            code = event["id"]
            name = event["name"]
            start_time = posix_to_normal(int(event["startTimeSeconds"]))
            end_time = posix_to_normal(int(event["startTimeSeconds"]) + int(event["durationSeconds"]))
            platform = "codeforces"
            contest_url = 'http://codeforces.com/contest/' + str(code)
            resultSet["upcoming_contests"].append({"code":code,"platform":platform,"name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})
        else:
            code = event["id"]
            name = event["name"]
            start_time = event["startTimeSeconds"]
            end_time = event["durationSeconds"]
            platform = "codeforces"
            contest_url = 'http://codeforces.com/contest/' + str(code)
            resultSet["present_contests"].append({"code":code,"platform":platform,"name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})

if __name__ == '__main__':
    scrape()