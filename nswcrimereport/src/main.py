#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

import sys
import html
from crawler import generate_news_list
from crimegmaps import CrimeGMaps


def main():
    crimeList = generate_news_list()
    for crime in crimeList:
        for idx in range(5):
            print "crime[" + str(idx) +"] : ", str(crime[idx])
        print "----------------------------------------------------------"
    
    header = html.getHeader()
    gmap = CrimeGMaps(crimeList)
    option = gmap.optionStr()
    latlng = gmap.latLngStr()
    places = gmap.placeStr()
    infoWindow = gmap.infoWindowStr()
    body = option + latlng + places + infoWindow
    footer = html.getFooter()
    
    html.makeHTML(header, body, footer)
    print "NSW crime news page updated"

if __name__ == '__main__':
    status = main()
    sys.exit(status)