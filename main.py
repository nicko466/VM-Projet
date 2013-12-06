#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from exportData import *
from color import *
from shepard import *


class Station : 
  def __init__(self, pt, name):
    self.pt = pt
    self.name = name
    
  def __repr__(self):
    return " - " + self.name + " {x: " + str((self.pt.x)) + " y:" + str((self.pt.y)) + " v:" + str (int(self.pt.val)) + "}"


################# On crée nos XI ####################
# x1Part= 0.20
# xmin = XI("rgb",20, 20, 20, min([min(l) for l in matrixData]))
# xmax = XI("rgb",200, 0, 200, max([max(l) for l in matrixData]))
# x1 = XI("rgb",50, 50, 0, (xmax.value-xmin.value)* (x1Part) + xmin.value)
# x2 = XI("rgb",0, 100, 100, (xmax.value-xmin.value)* (x1Part) + x1.value)
# x3 = XI("rgb",150, 150, 150, (xmax.value-xmin.value)* (x1Part) + x2.value)

# ech = []
# ech.append(xmin)
# ech.append(x1)
# ech.append(x2)
# ech.append(x3)
# ech.append(xmax)
######################################################

# tabRGB = generateRGB(matrixData, ech)
# matrixRgb2Image(tabRGB,"image")


# dataTab = lectureData("data.txt")
# print "dataTab",dataTab

#===============================================================================
# Crée une matrice de station depuis les données CSV
#===============================================================================
def makeStationsData(matriceRaw):
	matPoint = []
	for i in range(0, len(matriceRaw)):
		tabPoint = []
		for j in range(4, len(matriceRaw[i])):
			name = matriceRaw[i][0]
			x = matriceRaw[i][1]
			y = matriceRaw[i][2]
			val = matriceRaw[i][j]
			station = Station(Point(x, y, val), name)
			tabPoint.append(station)
		matPoint.append(tabPoint)
	return matPoint
					
def selectZoneReference(matriceStation):
    minX = matriceStation[0][0].pt.x
    minY = matriceStation[0][0].pt.y
    maxX = matriceStation[0][0].pt.x
    maxY = matriceStation[0][0].pt.y
    
    for i in range(0, len(matriceStation)):
        minX = min (matriceStation[i][0].pt.x, minX)
        minY = min (matriceStation[i][0].pt.y, minY)
        maxX = max (matriceStation[i][0].pt.x, maxX)
        maxY = max (matriceStation[i][0].pt.y, maxY)
        # print "xmin", minX , "xmax", maxX, "ymin", minY , "ymax", maxY
    ptMin = Point(minX , minY, 0)
    ptMax = Point(maxX , maxY, 0)
    return (ptMin, ptMax )
    

#===============================================================================
# Shepard a un instant t
#===============================================================================
def shepardOneTime(stationMatrice, t, ptMin, ptMax, pas):
    tabPointGenere = []
    tabData = []
    # stations vers points
    for stat in stationMatrice :
        tabData.append(stat[t].pt)
        
    i = ptMin.x
    while i < ptMax.x:
        j = ptMin.y
        while j < ptMax.y:
            pt = Point(i, j, 0)
            pt.val = shepard(pt, tabData)
            tabPointGenere.append(pt)
            j = j + pas
        i = i + pas
    print  tabPointGenere


# pt =Point(x,y,0)
# pt.val=shepard(pt,dataTab)
# tabPointGenere.append(pt)       
data = getMatriceData()
matStation = makeStationsData(data)
# print matStation[0][0].pt
(ptMin, ptMax) = selectZoneReference(matStation)
print (ptMin, ptMax)
shepardOneTime(matStation, 0, ptMin, ptMax, 0.1)








