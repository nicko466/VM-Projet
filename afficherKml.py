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

def createKML(x0, x1, y0, y1, tabIsovalue):
    pathToKML = "KML/"
    print " x0 :",x0," x1 :",y0," y1 :",y1
    fichier = open(pathToKML + "/timeStampPollution.kml", "w")
    month = "08"
    nextMonth = "08"
    day = "01"
    nextDay = "02"

    monkml ="""<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
    \n<Folder>
    <name>Views with Time</name>
    <description></description>"""
    for i in range(1,8):
        if i<8:
            day = "0"+str(i)
            nextDay = "0"+str(i+1)
        else:
            day = str(i)
            nextDay = str(i+1) 
        
        monkml += """
        <GroundOverlay>
            <name>GroundOverlay"""+str(i)+ """</name>
            
            <TimeSpan>
                <begin>2012-"""+month+"""-"""+day+"""</begin>
                <end>2012-"""+nextMonth+"""-"""+nextDay+"""</end>
            </TimeSpan>
            <Icon>
                <href>../imagesResult/image"""+str(i)+""".png</href>
            </Icon>
            <LatLonBox>
        <north>"""+str(y1)+"""</north>
        <south>"""+str(y0)+"""</south>
        <east>"""+str(x1)+"""</east>
        <west>"""+str(x0)+"""</west>
        <rotation>0.0</rotation>
      </LatLonBox>""" 
            
            
           # <gx:LatLonQuad>
           #     <coordinates>4.07,46.21,0.0 6.87,46.21,0.0 6.87,44.35,0.0 4.07,44.35,0.0</coordinates>
           # </gx:LatLonQuad>"""
             
            
            
            
        
       
        monkml += "</GroundOverlay>\n" 
       
        for segment in tabIsovalue[i]: # On parcours le tableau pour chaque t
                monkml += """ <Placemark> <TimeSpan>
                    <begin>2012-"""+month+"""-"""+day+"""</begin>
                    <end>2012-"""+nextMonth+"""-"""+nextDay+"""</end>
                    </TimeSpan> """
             # Pour chaque segment
                monkml += "<LineString><coordinates>"
                monkml += str(segment.x1) + "," + str(segment.y1) + ",0 " + str(segment.x2) + "," + str(segment.y2) + ",0\n"
                monkml += " </coordinates></LineString></Placemark>"
    monkml += '\n</Folder></kml>'
    fichier.write(monkml)
    
    
