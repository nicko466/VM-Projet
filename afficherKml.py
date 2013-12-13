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

def createKML(pathImage,x0,x1,y0,y1):
    pathToKML = "KML/"
    fichier = open(pathToKML+"/timeStampPollution.kml", "w")
    fichier.write('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">')
    fichier.write('\n')
    fichier.write('<Document><name>Views with Time</name><open>1</open><description></description>')
    
    for i in range(1,20):
        fichier.write(
                      '<Document id="feat_1">'+
        '<name>KmlUsage</name>'+
        '<GroundOverlay id="feat_2">'+
            '<name>GroundOverlay</name>'+
            '<Icon id="link_0">'+
                '<href>../imagesResult/image'+str(i)+'.png</href>'+
            '</Icon>'+
            '<TimeStamp>'+
                '<when>2005-02-21T08:'+str(i)+':10Z</when>'+
            '</TimeStamp>'+
            '<gx:LatLonQuad>'+
             '   <coordinates>4.07,46.21,0.0 6.87,46.21,0.0 6.87,44.35,0.0 4.07,44.35,0.0</coordinates>'+
            '</gx:LatLonQuad>'+
        '</GroundOverlay>'+
    '</Document>')
        fichier.write('\n')
    fichier.write('</Document>')
    fichier.write('</kml>')
    
    
