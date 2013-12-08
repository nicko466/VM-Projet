#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from exportData import *
from color import *
from shepard import *
from afficherKml import *

#===============================================================================
# une station = point + nom
#===============================================================================
class Station : 
  def __init__(self, pt, name):
    self.pt = pt
    self.name = name
    
  def __repr__(self):
    return " - " + self.name + " {x: " + str((self.pt.x)) + " y:" + str((self.pt.y)) + """ 
    v:""" + str (int(self.pt.val)) + "}"


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

#===============================================================================
# Selectionne le point min , max des stations pour trovuer la zone à étudier
#===============================================================================
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

    ptMin = Point(minX , minY, 0)
    ptMax = Point(maxX , maxY, 0)
    return (ptMin, ptMax)

  #=============================================================================
  # retourne le point minimum de la matrice de point
  #=============================================================================
def minMatrixPoint(matrix):
    mini = matrix[0][0].val
    for i in matrix:
        for j in i:
            if mini >j.val:
                mini =j.val
    return mini

#===============================================================================
# retourne le point maximum de la matrice de point
#===============================================================================
def maxMatrixPoint(matrix):
    maxi = 0
    for i in matrix:
        for j in i:
            if maxi < j.val:
                maxi = j.val
    return maxi

#===============================================================================
# Shepard a un instant t
#
# @param stationMatrice: ma matrice de donnée {station x t}
# @param t: l'indice du temps selectionné
# @param ptMax: ldes stations
# @param ptMin: des stations
# @param pas: float du pas de précision
# @return une matrice de tout les points
#===============================================================================
def shepardOneTime(stationMatrice, t, ptMin, ptMax, pas):
    matPointGenere = []
    tabData = []
    # Stations vers points
    for stat in stationMatrice :
        tabData.append(stat[t].pt)
        
    i = ptMin.x
    print tabData;
    while i < ptMax.x:
        j = ptMin.y
        tabPoint = []
        while j < ptMax.y:
            pt = Point(i, j, 0)
            pt.val = shepard(pt, tabData)
            tabPoint.append(pt)
            j = j + pas
        i = i + pas
        matPointGenere.append(tabPoint)
    print "taille", len(matPointGenere),len(matPointGenere[0]), "from", len(stationMatrice), len(stationMatrice[0])  
    return matPointGenere

################# Main ####################
# On recup notre data     
print "Récupération des données..."
data = getMatriceData()
print "Analyse"
# data vers matrice de station
matStation = makeStationsData(data)
# on definit la zone de visualisation
(ptMin, ptMax) = selectZoneReference(matStation)
# On determine la valeur des points de la zone
print 'ptMin, ptMax',ptMin, ptMax
pas = 0.1
matrixData = shepardOneTime(matStation, 0, ptMin, ptMax, pas)
mini = minMatrixPoint(matrixData)
maxi = maxMatrixPoint(matrixData)

################# On crée nos XI ####################
x1Part = 0.20
xmin = XI("rgb", 200, 200, 200, mini)
xmax = XI("rgb", 50, 0, 200, maxi)
x1 = XI("rgb", 100, 50, 0, (xmax.value - xmin.value) * (x1Part) + xmin.value)
x2 = XI("rgb", 0, 100, 20, (xmax.value - xmin.value) * (x1Part) + x1.value)
x3 = XI("rgb", 150, 150, 150, (xmax.value - xmin.value) * (x1Part) + x2.value)


ech = []
ech.append(xmin)
ech.append(x1)
ech.append(x2)
ech.append(x3)
ech.append(xmax)
######################################################
print "matrixData",len(matrixData),len(matrixData[0])
matRGB = generateRgbFromPointMatrix(matrixData, ech)
print "img",len(matRGB),len(matRGB[0])
matrixRgb2Image(matRGB, "image")
#Permet de créer un fichier kml 
createKML("image.png",ptMin.x,ptMax.x,ptMin.y,ptMax.y)








