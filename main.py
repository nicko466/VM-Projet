#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from exportData import *
from color import *
from shepard import *
from afficherKml import *
from isoValueMap import *
import sys

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
            if mini > j.val:
                mini = j.val
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

    print """=====================================
Avancement du traitement des données
=====================================
0.00 %"""
    # on parcours selon le pas
    while i < ptMax.x:
        j = ptMin.y
        tabPoint = []
        while j < ptMax.y:
            # on crée un nouveau point
            pt = Point(i, j, 0)
            # on sheparde pour avoir sa valeur
            pt.val = shepard(pt, tabData)
            # On sauvegarde le point
            tabPoint.append(pt)
            j = j + pas
        i = i + pas
        matPointGenere.append(tabPoint)
        
        # On affiche le pourcentage d'avancement
        if (((i - ptMin.x) / (ptMax.x - ptMin.x)) * 100) < 100:
            print ("%.2f" % (((i - ptMin.x) / (ptMax.x - ptMin.x)) * 100)), "%"


    data = []
    for row in matPointGenere:
		data.append(row[t])

    isoValue = 9
    signes = determinePlusLess(data, isoValue)
    nbRow = len(matPointGenere)
    nbCol = len(matPointGenere[0])
    tabSegment = marchingSquare(data, signes, isoValue, nbCol, nbRow)
    drawPS(data, tabSegment, nbCol, int(nbRow))

    return matPointGenere

#===============================================================================
# Launch analyse
#===============================================================================
def analyseOneTime(matStation, tSelect, ptMin, ptMax, pas):
    matrixData = shepardOneTime(matStation, tSelect, ptMin, ptMax, pas)
    mini = minMatrixPoint(matrixData)
    maxi = maxMatrixPoint(matrixData)
    
    ################# On crée nos XI ####################

    xmin = XI("rgb", 0, 0, 255, mini)
    xmax = XI("rgb", 200, 0, 0, maxi)
    x1 = XI("rgb", 63, 0, 175, (xmax.value - xmin.value) * (0.001) + xmin.value)
    x2 = XI("rgb", 125, 0, 125, (xmax.value - xmin.value) * (0.005) + xmin.value)
    x3 = XI("rgb", 195, 0, 63, (xmax.value - xmin.value) * (0.25) + xmin.value)

    ech = []
    ech.append(xmin)
    ech.append(x1)
    ech.append(x2)
    ech.append(x3)
    ech.append(xmax)
    ######################################################
    
    matRGB = generateRgbFromPointMatrix(matrixData, ech)
    matrixRgb2Image(matRGB, ("imagesResult/image" + str(tSelect)))
    # Permet de créer un fichier kml 
    createKML(("imagesResult/" + str(tSelect)) + ".png", ptMin.x, ptMax.x, ptMin.y, ptMax.y)

########### Selon les arguments ###########
# python main.py [pas] [tselect]
if len(sys.argv) <= 1:
    pas = 0.1  
    tSelect = 0 
    print "pas=", pas, "=t", tSelect
    
if len(sys.argv) == 2:
    pas = float(sys.argv[1])
    tSelect = 0
    print "pas=", pas, "=t", tSelect
    
if len(sys.argv) == 3:
    pas = float(sys.argv[1])
    if sys.argv[2] == "all" :
        tSelect = -1
    else:
        tSelect = int(sys.argv[2])
    print "pas=", pas, "t=", tSelect

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
print 'ptMin, ptMax', ptMin, ptMax


if tSelect == -1 :
    for tSelect in range (0, len(matStation[0])):
        analyseOneTime(matStation, tSelect, ptMin, ptMax, pas)
else:
    analyseOneTime(matStation, tSelect, ptMin, ptMax, pas)






