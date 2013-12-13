#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from simplekml import Kml

#===============================================================================
# Fonction createKml qui "colle" l image (dont le chemin est pathimage) avec les coordonnees
#             
#                (x0,y1)--(x1,y1)
#                   |       |
#                   |       |
#                   |       |
#                (x0,y0)--(x1,y0)
#
#===============================================================================

def createKML(pathImage,x0,x1,y0,y1, isovalue):
    pathToKML = "KML/"
    fichier = open(pathToKML+"/timeStampPollution.kml", "w")
    
    monkml ="""<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" >
    \n<Folder>
    <name>Views with Time</name>
    
    <description></description>"""
    
    for i in range(1,9):
        monkml += """
        <GroundOverlay>
            <name>GroundOverlay"""+str(i)+ """</name>
            
            <TimeSpan>
                <begin>2004-0"""+str(i)+"""</begin>
                <end>2004-0"""+str(i+1)+"""</end>
            </TimeSpan>
            <Icon>
                <href>../imagesResult/image"""+str(i)+""".png</href>
            </Icon>
            
            <gx:LatLonQuad>
                <coordinates>4.07,46.21,0.0 6.87,46.21,0.0 6.87,44.35,0.0 4.07,44.35,0.0</coordinates>
            </gx:LatLonQuad>
        </GroundOverlay>"""
        monkml += "\n"
   # for segment in isovalue:
    #        monkml += "<Placemark><LineString><coordinates>"
     #       monkml += str(segment.x1) +" , " + str(segment.y1) + " , 0.\n"
      #      monkml += str(segment.x1) +" , " + str(segment.y1) + " , 0.\n"
       #     monkml += " </coordinates></LineString></Placemark>"
    monkml += '\n</Folder></kml>'
    fichier.write(monkml)
    
    
