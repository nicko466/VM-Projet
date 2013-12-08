#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import math
import exceptions

muI= 2 #ou 2

#===============================================================================
# classe Point
#===============================================================================
class Point : 
  def __init__(self, x, y,val):
    self.x = float(x)
    self.y = float(y)
    try:
    	self.val = float(val)
    except exceptions.ValueError:
	self.val = -1.0
    
  def __repr__(self):
    return "{x: " +str((self.x)) + " y:" + str((self.y)) + " v:" + str (int(self.val))+"}"

#===============================================================================
# norme d'un point
#===============================================================================
def norme(point):
    return math.sqrt(point.x * point.x + point.y * point.y)

#===============================================================================
# norme d'un vecteur de deux point
#===============================================================================
def distance (pOrig,p2):
    pf = Point( pOrig.x- p2.x, pOrig.y -p2.y,0.0)
    return norme (pf)

#===============================================================================
# créer une matrice avec la distance de chaque point par rapport
# à celui de référence
#===============================================================================
def creerTabDistance (tabPoint, point):
    tabRes =[]
    for i in range (0, len(tabPoint)):
        dist =distance(point,tabPoint[i])
        if dist !=0:
            tabRes.append(dist)
    return tabRes


def calculOmega(tabDist,i):
    numerateur= 1
    for j in range (0,len(tabDist)):
        if j!=i:
            numerateur *=pow(tabDist[j],muI)
    
    denominateur =0
    for k in range (0,len(tabDist)):
        res= 1
        for j in range (0,len(tabDist)):
            if j!=k:
                res *=pow(tabDist[j],muI)
        denominateur += res
        
    return numerateur/denominateur

#===============================================================================
# lance l'algo de shepard pour un point par rapport à un
# tableau de valeurs de référence
#===============================================================================
def shepard(point, dataTab):
    tabDist = creerTabDistance(dataTab, point) 
    
    res=0
    for i in range(0,len(dataTab)):
        omega= calculOmega(tabDist,i)
        res+= dataTab[i].val * (omega)
    return res
    



    
