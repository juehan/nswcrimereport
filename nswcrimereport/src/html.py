HEADER = '<!DOCTYPE html><html><head>\n\
          <meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\" />\n\
          <style type=\"text/css\">\n\
            html { height: 100% }\n\
            body { height: 90%; margin: 5; padding: 5 }\n\
            #map_canvas { height: 100% }\n\
          </style>\n\
          <script type=\"text/javascript\"\n\
             src="http://maps.googleapis.com/maps/api/js?key=AIzaSyDUWg0EnNMSjHXKFMXMRiHR_V3enb5qMho&sensor=false\">\n\
          </script>\n\
          <script type=\"text/javascript\">\n' 

FOOTER = '<body onload=\"initialize()\">\n\
            <div id=\"map_canvas\" style=\"width:100%; height:100%\"></div>\n\
            <br>Data will be Updated every hour\n\
          </body></html>'

def getHeader():
  return HEADER


def getFooter():
  return FOOTER


def makeHTML(header, body, footer):
  f = open("crimenews.html", "w")
  f.write(header+body+footer)
  
