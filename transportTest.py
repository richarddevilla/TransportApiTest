import requests
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv
from google.transit import gtfs_realtime_pb2


##myreq = requests.get('https://myhomelivingcare.supportability.com.au',auth=HTTPDigestAuth('mhlc','mh1c'))
##c = myreq.content
##s = myreq.cookies
##
##loginscr = requests.get('https://myhomelivingcare.supportability.com.au/staffAccountEdit.php?x=247700861',auth=HTTPBasicAuth('richard.devilla','Teku0831'),cookies=s)
##b = loginscr.content
##y = myreq.cookies
##
##payload = {'formAction': 'exportShiftData', 'step': '2', 'scheduleType': 'systemuser','systemuserID': 'All','clientID': 'All','fromDate':'20170612000000','toDate':'20170619000000'}
##x = requests.post("https://myhomelivingcare.supportability.com.au/system/inc/custom/reports/activityScheduleReport.php", data=payload,cookies=y)
##
headers= {'Authorization': 'apikey cYYUJIy0P5wuNLTe5KPG1jtOKlL6VroLGN3Z'}
wLine = requests.get("https://api.transport.nsw.gov.au/v1/gtfs/realtime/buses",headers=headers)

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(wLine.content)

lineOutput = []
   
with open( 'test.html', 'w',newline = "") as f:
    for xLine in feed.entity:
        writer = csv.writer(f)
        #lineOutput.append(xLine)
        writer.writerow(str(xLine))
        
#xLine.trip_update.stop_time_update[1].arrival.delay
