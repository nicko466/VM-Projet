#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import colorsys
import math
import Image
import random


# Object point
class XI:
	def __init__(self, typeColor, a, b, c, value):
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
# non utilise
def matrixHsv2matrixRgb(m):
	tabRGB = []
	for i in range(0, len(m)):
		itabRGB = []
		for j in range(0, len(m)):
			(h, s, v) = m[i][j]
			r, g, b = colorsys.hsv_to_rgb(h, s, v)
			itabRGB.append((r, g, b))
		tabRGB.append(itabRGB)
	return tabRGB

# non utilise
def matrixRgb2MatrixHsv(m):
	tabHSV = []
	for i in range(0, len(m)):
		itabHSV = []
		for j in range(0, len(m)):
			(r, g, b) = m[i][j]
			h, s, v = colorsys.rgb_to_hsv(r, g, b)
			itabHSV.append((h, s, v))
		tabHSV.append(itabHSV)
	return tabHSV


# fonction d'interpolation 
# @param [a, b] l'encadrement
# @param v1 valeur de a
# @param v2 valeur de b
# @param x indice
# @return la valeur de x
def interpolation (a, b, v1, v2, x):
	if v1 == v2:
		#print "equal"
		return 0
	return ((v2 - x) / (v2 - v1)) * a + ((x - v1) / (v2 - v1)) * b 

# genere la matrice RGB depuis un tableau de point
# @param mat la matrice de donnée
# @param echelle une liste des XI
# @return la matrice RGB
def generateRgbFromPointMatrix(mat, echelle):
	matRGB = []
	for i in range(0, len(mat)):
        	itabRGB = []
        	for j in range(0, len(mat[0])):
			# pour tout elt de la matrice
			xIndMin = 0
			# On recherche la place de la valeur
			for k in range(1, len(echelle)-1):
				if  mat[i][j].val > echelle[k].value :
					xIndMin = k
		            
			if xIndMin+1 < len(echelle):
				x = echelle[xIndMin]
				x1 = echelle[xIndMin + 1]
				hi = interpolation(x.h, x1.h, x.value, x1.value, mat[i][j].val)
				si = interpolation(x.s, x1.s, x.value, x1.value, mat[i][j].val)
				vi = interpolation(x.v, x1.v, x.value, x1.value, mat[i][j].val)
			else:
				hi = 55
				si = 55
				vi = 55
			(ri, gi, bi) = colorsys.hsv_to_rgb(hi, si, vi)
			#print ri, gi, bi, hi, si, vi
			itabRGB.append((ri, gi, bi))
		matRGB.append(itabRGB)
	return matRGB

# genere la matrice RGB
# @param mat la matrice de donnée
# @param echelle une liste des XI
# @return la matrice RGB
def generateRGB(mat, echelle):
	tabRGB = []
	for i in range(0, len(mat)):
		itabRGB = []
		for j in range(0, len(mat)):
			xIndMin = 0
			for k in range(1, len(echelle)):
				if  mat[i][j] > echelle[k].value :
					xIndMin = k

			x = echelle[xIndMin]
			x1 = echelle[xIndMin + 1]
			hi = interpolation(x.h, x1.h, x.value, x1.value, mat[i][j])
			si = interpolation(x.s, x1.s, x.value, x1.value, mat[i][j])
			vi = interpolation(x.v, x1.v, x.value, x1.value, mat[i][j])
			(ri, gi, bi) = colorsys.hsv_to_rgb(hi, si, vi)
			itabRGB.append((ri, gi, bi))
		tabRGB.append(itabRGB)
	return tabRGB

# matrice RGB vers une image de nom namefile.png
# @param m : la matrice
# @param nameFile : le path sans extension du fichier de sortie
def matrixRgb2Image(m, nameFile):
	size = (len(m), len(m[0]))
	im = Image.new('RGBA', size)
	pix = im.load()
	for i in range(size[0]):
	    for j in range(size[1]):
		localOpacity = min((255-int(m[i][j][2]))*3,255)
		pix[i, j] = (int(m[i][j][0]), int(m[i][j][1]), int(m[i][j][2]),localOpacity) 
	im.save(nameFile + ".png")
	print nameFile + ".png" + " created !"





