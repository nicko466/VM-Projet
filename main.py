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
    return " - " +name + " {x: " + str((self.pt.x)) + " y:" + str((self.pt.y)) + " v:" + str (int(self.pt.val))+"}"


################# On crée nos XI ####################
#x1Part= 0.20
#xmin = XI("rgb",20, 20, 20, min([min(l) for l in matrixData]))
#xmax = XI("rgb",200, 0, 200, max([max(l) for l in matrixData]))
#x1 = XI("rgb",50, 50, 0, (xmax.value-xmin.value)* (x1Part) + xmin.value)
#x2 = XI("rgb",0, 100, 100, (xmax.value-xmin.value)* (x1Part) + x1.value)
#x3 = XI("rgb",150, 150, 150, (xmax.value-xmin.value)* (x1Part) + x2.value)

#ech = []
#ech.append(xmin)
#ech.append(x1)
#ech.append(x2)
#ech.append(x3)
#ech.append(xmax)
######################################################

#tabRGB = generateRGB(matrixData, ech)
#matrixRgb2Image(tabRGB,"image")


#dataTab = lectureData("data.txt")
#print "dataTab",dataTab

def makeStationsData(matriceRaw):
	matPoint = []
	for i in range(0,len(matriceRaw)):
		tabPoint = []
		for j in range(4,len(matriceRaw[i])):
			name = matriceRaw[i][0]
			x = matriceRaw[i][1]
			y = matriceRaw[i][2]
			val = matriceRaw[i][j]
			station=Station(Point(x,y,val), name)
			print name, i , j
			tabPoint.append(station)
		matPoint.append(tabPoint)
	return matPoint
					


def ShepardOneColumn(columData):
	tabPoint = []
	for i in range(0,len(columData)):
		pt =Point(x,y,0)
		pt.val=shepard(pt,dataTab)		

tabPointGenere= []

#pt =Point(x,y,0)
#pt.val=shepard(pt,dataTab)
#tabPointGenere.append(pt)       
 
data = getMatriceData()
#print data[1]
matPoint = makeStationsData(data)









