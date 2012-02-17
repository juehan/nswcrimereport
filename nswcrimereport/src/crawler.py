# -*- coding:utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup
from geopy import geocoders
import time
import re

def HasDash(mystr):
  location = mystr.find('-')
  if location is not -1:
    if mystr[location+1] == " ":
      return True
  return False

def IsValidLocation(rawlocation):
  locationlist =  rawlocation.split(' ')
  if len(locationlist) > 2:
    return False
  else:
    return True
  
# \u2010 : HYPHEN
# \u2013 : EN DASH
# \u2014 : EM DASH
def AnalyzeTitle(title):
  hasDash = HasDash(title)
  if hasDash:
    location = title.find('-')
    strCrime = title[:location - 1];
    if IsValidLocation(title[location + 2:]):
      strLocation = title[location + 2:] + ", NSW, Australia"
    else:
      strLocation = ""
    return (strCrime, strLocation)
  else:
    return ("", "")

  
def GetLatLngList(location):
  LatLng = []
  g = geocoders.Google(resource = 'maps')
  
  try:    
    places, (lat, lng) = g.geocode(location)
    time.sleep(0.1)
    LatLng.append("%.5f" % lat)
    LatLng.append("%.5f" % lng)
  except Exception as e:
#    x = "Didn't find exactly one placemark!"
#    if str(e).find(x) >= 0:
#      places, (lat, lng) = g.geocode(location, exactly_one=False)
#      #places = g.geocode(location, exactly_one=False)
#      time.sleep(0.1)
#      LatLng.append("%.5f" % places[1][0])
#      LatLng.append("%.5f" % places[1][1])
#      log = open('logfile.txt', 'a')
#      s = 'location: {0}, Exception: {1}'.format(location, e)
#      log.write('%s\n' %s)
#      log.close()
#    else:
#      log = open('logfile.txt', 'a')
#      s = 'location: {0}, Exception: {1}'.format(location, e)
#      log.write('%s\n' %s)
#      log.close()
  
    log = open('logfile.txt', 'a')
    s = 'location: {0}, Exception: {1}'.format(location, e)
    log.write('%s\n' %s)
    log.close()

  return LatLng
  

newsSite = 'http://m.police.nsw.gov.au/news'

def GenerateNewsList():
  html_source = urllib2.urlopen(newsSite)
  soup = BeautifulSoup(html_source.read())
  newsList = []
  for i in range (2,32):
    htmltext = soup('li')[i]
    weblink = htmltext('a')[0]['href']
    info = htmltext.findAllNext(text = True)
    date = info[2]
    strCrime, strLocation = AnalyzeTitle(info[1])
    latLng = GetLatLngList(strLocation)
     
    if strCrime and strLocation and len(latLng) > 0:
      news = []
      if re.search('"', strCrime) or re.search("'", strCrime) :
        strCrimeEscaped = re.escape(strCrime)
        news.append(strCrimeEscaped)
      else: 
        news.append(strCrime)
      news.append(strLocation)
      news.append(weblink)      
      news.append(date)
      news.append(latLng)
      newsList.append(news)
  return newsList



    


