import sys
import html
from crawler import GenerateNewsList
from crimegmaps import CrimeGMaps


def main():
  crimeList = GenerateNewsList()
  for crime in crimeList:
    for x in range(5):
      print "crime[" + str(x) +"] : ", str(crime[x])
    print "----------------------------------------------------------"
    
  getHeader = html.getHeader()
  
  gmap = CrimeGMaps(crimeList)
  
  option = gmap.optionStr()
  latlng = gmap.latLngStr()
  places = gmap.placeStr()
  infoWindow = gmap.infoWindowStr()
  body = option + latlng + places + infoWindow
    
  footer = html.footer()

  html.makeHTML(getHeader, body, footer)
  print "NSW crime news page updated"

if __name__ == '__main__':
  status = main()
  sys.exit(status)