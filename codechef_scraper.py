import urllib2
import json
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime

def scrape(resultSet):
    url = 'https://www.codechef.com/contests'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")

    result = []
    tableList = soup.findAll("table",attrs = {"class":"dataTable"})  #listofAllLinks
    contestTypes = soup.findAll("h3");

    i = 0
    present_contests = []
    upcoming_contests = []
    for contest in contestTypes:
        if(contest.get_text() == 'Present Contests'):
            present_contests = tableList[i].findAll("tr")
        elif(contest.get_text() == 'Future Contests'):
            upcoming_contests = tableList[i].findAll("tr")
        i = i+1


    #present_contests = tableList[0].findAll("tr")  #present contests
    if(len(present_contests) > 0 ):
        for contest in present_contests[1:]:
            event_details_row = contest.findAll("td")
            code = event_details_row[0].string
            name = event_details_row[1].string
            start_time = parse(event_details_row[2]['data-starttime']).strftime("%Y-%m-%d %H:%M:%S")
            end_time = parse(event_details_row[3]['data-endtime']).strftime("%Y-%m-%d %H:%M:%S")
            contest_url = "www.codechef.com/" + code
            resultSet["present_contests"].append({"code":code,"platform":"codechef","name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})


    #upcoming_contests = tableList[1].findAll("tr")  #upcoming contests
    if(len(upcoming_contests) > 0 ):
        for contest in upcoming_contests[1:]:
            event_details_row = contest.findAll("td")
            code = event_details_row[0].string
            name = event_details_row[1].string
            start_time = parse(event_details_row[2]['data-starttime']).strftime("%Y-%m-%d %H:%M:%S")
            end_time = parse(event_details_row[3]['data-endtime']).strftime("%Y-%m-%d %H:%M:%S")
            contest_url = "www.codechef.com/" + code
            resultSet["upcoming_contests"].append({"code":code,"platform":"codechef","name":name,"start_time":start_time,"end_time":end_time,"contest_url":contest_url})        

if __name__ == '__main__':
    scrape()