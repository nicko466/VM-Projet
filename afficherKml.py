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
    
    monkml ="""<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
    \n<Document>
    <name>Views with Time</name>
    <open>1</open>
    <description></description>"""
    
    for i in range(1,20):
        monkml += """<Document id="feat_1">
        <name>KmlUsage</name>
        <GroundOverlay id="feat_2">
            <name>GroundOverlay</name>
            <Icon id="link_0">
                <href>../imagesResult/image"""+str(i)+""".png</href>
            </Icon>
            <TimeStamp>'+
                <when>2005-02-21T08:"""+str(i)+""":10Z</when>
            </TimeStamp>
            <gx:LatLonQuad>
                <coordinates>4.07,46.21,0.0 6.87,46.21,0.0 6.87,44.35,0.0 4.07,44.35,0.0</coordinates>
            </gx:LatLonQuad>
        </GroundOverlay>"""
        for segment in isovalue:
            monkml += "<Placemark><LineString><coordinates>"
            monkml += str(segment.x1) +" , " + str(segment.y1) + " , 0.\n"
            monkml += str(segment.x1) +" , " + str(segment.y1) + " , 0.\n"
            monkml += " </coordinates></LineString></Placemark>"
            
        monkml += "</Document>\n"
    monkml += '\n</Document></kml>'
    fichier.write(monkml)
    
    
