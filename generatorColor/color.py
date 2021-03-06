#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import colorsys
import math
import Image
import random

#Object point
class XI:
	def __init__(self,typeColor, a, b, c, value):
		if typeColor == "rgb":
			self.r = a
			self.g = b
			self.b = c
			self.h, self.s, self.v = colorsys.rgb_to_hsv(a, b, c)
		else:
			if typeColor == "hsv":
				self.h = a
				self.s = b
				self.v = c
				self.r, self.g, self.b = colorsys.hsv_to_rgb(a, b, c)
		self.value = value
#non utilise
def matrixHsv2matrixRgb(m):
	tabRGB = []
	for i in range(0,len(m)):
		itabRGB = []
		for j in range(0,len(m)):
			(h, s, v) = m[i][j]
			r,g,b = colorsys.hsv_to_rgb(h, s, v)
			itabRGB.append((r,g,b))
		tabRGB.append(itabRGB)
	return tabRGB

#non utilise
def matrixRgb2MatrixHsv(m):
	tabHSV = []
	for i in range(0,len(m)):
		itabHSV = []
		for j in range(0,len(m)):
			(r, g, b) = m[i][j]
			h, s, v = colorsys.rgb_to_hsv(r, g, b)
			itabHSV.append((h,s,v))
		tabHSV.append(itabHSV)
	return tabHSV

#fonction appliquee
def fun (i,j):
	return math.sin(math.pi * i /128 + math.pi * j /128 )

#genere l ensemble de donnees
# @param size : la taille de la matrice generee
def generateData(size, fun):
	tab = []
	for i in range(0,size):
		itab= []
		for j in range(0,size):
			itab.append(fun(i,j))
		tab.append(itab)
	return tab

# fonction d'interpolation 
# @param [a, b] l'encadrement
# @param v1 valeur de a
# @param v2 valeur de b
# @param x indice
# @return la valeur de x
def interpolation (a, b, v1, v2, x):
	if v1 == v2:
		return 0
	return ((v2 - x)/(v2-v1))*a + ((x-v1)/(v2-v1))*b 

# genere la matrice RGB
# @param mat la matrice de donnée
# @param echelle une liste des XI
# @return la matrice RGB
def generateRGB(mat, echelle):
	tabRGB = []
	for i in range(0,len(mat)):
		itabRGB= []
		for j in range(0,len(mat)):
			xIndMin = 0
			for k in range(1,len(echelle)):
				if  mat[i][j] > echelle[k].value :
					xIndMin = k

			x = echelle[xIndMin]
			x1 = echelle[xIndMin+1]
			hi = interpolation(x.h, x1.h,x.value, x1.value, mat[i][j])
			si = interpolation(x.s, x1.s, x.value, x1.value, mat[i][j])
			vi = interpolation(x.v, x1.v,x.value, x1.value, mat[i][j])
			(ri, gi, bi) = colorsys.hsv_to_rgb(hi, si, vi)
			itabRGB.append((ri,gi,bi))
		tabRGB.append(itabRGB)
	return tabRGB

# matrice RGB vers une image de nom namefile.png
# @param m : la matrice
# @param nameFile : le path sans extension du fichier de sortie
def matrixRgb2Image(m, nameFile):
	size = (len(m),len(m[0]))
	im = Image.new('RGB',size)
	pix = im.load()
	for i in range(size[0]):
	    for j in range(size[1]):
		pix[i,j] = (int(m[i][j][0]), int(m[i][j][1]), int(m[i][j][0])) 
	im.save(nameFile + ".png")
	print nameFile + ".png" + " created !"

	
def xplus(i,j):
	return i+j

matrixData = generateData(512, fun)
################# On crée nos XI ####################
x1Part= 0.20
xmin = XI("rgb",20, 20, 20, min([min(l) for l in matrixData]))
xmax = XI("rgb",200, 0, 200, max([max(l) for l in matrixData]))
x1 = XI("rgb",50, 50, 0, (xmax.value-xmin.value)* (x1Part) + xmin.value)
x2 = XI("rgb",0, 100, 100, (xmax.value-xmin.value)* (x1Part) + x1.value)
x3 = XI("rgb",150, 150, 150, (xmax.value-xmin.value)* (x1Part) + x2.value)

ech = []
ech.append(xmin)
ech.append(x1)
ech.append(x2)
ech.append(x3)
ech.append(xmax)
######################################################
tabRGB = generateRGB(matrixData, ech)
matrixRgb2Image(tabRGB,"image")


