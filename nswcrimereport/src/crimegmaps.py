class CrimeGMaps:
  
  MAP_OPTION = """function initialize() {\n\
          var latlng = new google.maps.LatLng(-33.86469, 151.04363);\n\
          var myOptions = {\n\
              zoom: 6,\n\
              center: latlng,\n\
              mapTypeId: google.maps.MapTypeId.ROADMAP\n\
          };\n\
          var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n\
          var places = [];\n"""
          
  MAP_INFO_WINDOW = """var infoWindow;\n\n\
          for(var i = 0; i < places.length; i++){\n\
              var marker = new google.maps.Marker({\n\
                  position: places[i],\n\
                  map: map,\n\
                  title: \'NSW Crime\' + i\n\
              });\n\
              (function(i, marker){\n\
                  google.maps.event.addListener(marker, \'click\', function(){\n\
                    if(!infoWindow)\n\
                    {\n\
                      infoWindow = new google.maps.InfoWindow();\n\
                    }\n\
                    var content = \'<div id=\"info\">\' + \n\
                                  \'<h4>\'+ crimes[i][1] +\'</h4>\'+\n\
                                  \'<p>\'+ crimes[i][0]+\'</p>\'+\n\
                                  \'<p><i>\'+ crimes[i][3]+\'</i></p>\'+\n\
                                   \'<p><a href=\'+crimes[i][2]+\' target=\"_blank\">See more details</a></p>\'+\n\
                                  \'</div>\';\n\
                    infoWindow.setContent(content);\n\
                    infoWindow.open(map, marker);\n\
                    });\
              })(i, marker);\n\
          }\n\
          google.maps.event.trigger(marker, \'click\');\n\
        }\n\
       </script>\n\
    </head>\n"""
    
  
  def __init__(self, crimelist):
    self.crimeList = crimelist
  
    
  def optionStr(self):
    return self.MAP_OPTION
          
  
  def  infoWindowStr(self):
    return self.MAP_INFO_WINDOW

  
  def latLngStr(self):
    def func(c):
      mystr = 'places.push(new google.maps.LatLng(%s, %s))\n' % (c[4][0], c[4][1])
      return mystr
    result = ''.join(func(c) for c in self.crimeList)
    return result  


  def placeStr(self):
    numOfCrime = len(self.crimeList)
    arrayDecl = 'var crimes = new Array(' + str(numOfCrime) + ')\n\
                 for(var i = 0; i <' + str(numOfCrime) + ';i++){\n\
                    crimes[i] = new Array(4)\n\
                }\n'
    
    arrayItems = ""
    i = 0
    for crime in self.crimeList:
      for x in range(4):
        arrayItems += "crimes[" + str(i) + "][" + str(x) + "]=\"" + crime[x] + "\"\n"
      i = i + 1

    return arrayDecl + arrayItems