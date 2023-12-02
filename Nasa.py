import requests
import datetime
# import argparse
# import tkinter
import os
import sys
import subprocess
import urllib
from urllib.request import urlretrieve
from appscript import app, mactypes
# from tkinter import messagebox
from pprint import PrettyPrinter

# Change Background Script

cmd = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

creds = open('credentials.txt',"r")
content = creds.read()
creds.close()

pp = PrettyPrinter()
apiKey = content
URL_APOD = "https://api.nasa.gov/planetary/apod"
date = datetime.date.today()
# date = '2020-06-13'
params = {
        'api_key': apiKey,
        'date': date,
        'hd': 'True'}
response = requests.get(URL_APOD, params=params).json()
#pp.pprint(response)
is_picture = response["media_type"]
nasa_fact = response['explanation']
picName = response['title']
# print(is_picture)

event_response = requests.get('https://eonet.gsfc.nasa.gov/api/v3/events?status=open&limit=40',params={'api_key': apiKey}).json()
#pp.pprint(event_response)

ChartArray = []

for event in event_response['events']:
    array = []
    array.append(event['title'])
    array.append(event['categories'][0]['title'])
    array.append(str(event['geometry'][-1]['coordinates']))
    ChartArray.append(array)

#pp.pprint(ChartArray)


def subchange(picture):
    try:
        subprocess.Popen(cmd%picture,shell=True)
        #subprocess.call(["killall Dock"], shell=True)
    except KeyboardInterrupt:
        print("The Computer says NO!")


def change_desktop(photoName):
    photo_name = (str(photoName) + '-' + str(date) + '.png')
    file_path = os.path.join('/Users/justinsinger/Documents/NasaApp/photoStorage/',
                             photo_name)
    image_url = response['hdurl']
    urllib.request.urlretrieve(image_url, file_path)
    #print(response['hdurl'])
    subchange(file_path)

def change_desktop_random(file_path):
    photo_name = (str(photoName) + '-' + str(date) + '.png')
    file_path = os.path.join('/Users/justinsinger/Documents/NasaApp/photoStorage/',
                             photo_name)
    image_url = response['hdurl']
    urllib.request.urlretrieve(image_url, file_path)
    #print(response['hdurl'])
    subchange(file_path)

