import os
from shepard import Point

class Segment: 
    def __init__(self, x1, y1, x2, y2):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
    
    def __repr__(self):
        return "{(" + str((self.x1)) + ", " + str((self.y1))+ ")(" + str((self.x2)) + ", " + str((self.y2)) + ")}"
    
def lectureData(fich):
    fichier = open(fich, 'r') 
    tabPoint = []
    nbCol = 0
    nbRow = 0
    while True :
        line = fichier.readline()
        if line == '' :
          break
        (x, y, val) = line.split(" ")
        val =(val.split("\n"))[0]
        tabPoint.append( Point(x,y, val))
        if (nbCol < y):
            nbCol = int(y)
        if (nbRow < x):
            nbRow = int(x)
    return (tabPoint, nbCol, nbRow)

def determinePlusLess(tabPoint, valToCompare):
    tabSigne = []
    for i in range(0,len(tabPoint)):
        signe = 0
        if (tabPoint[i].val < valToCompare):
            signe = -1
        else :
            signe = +1
        tabSigne.append(signe)
    return tabSigne

def marchingSquare(tabPoint, tabSigne, isoVal, nbCol, nbRow):
    tabSegments = []
    mod = 0
    incMod = False 
    for i in range(0,len(tabPoint) - (nbCol+2)):
#        print (i%nbCol)
        if ((i >= nbCol) & (i % nbCol == mod)):
#            print mod, "i", i
            incMod = True
            continue
        elif (incMod):
            mod = mod + 1
            incMod = False
       
        indexp1 = i
        indexp2 = i+1
        indexp3 = i+nbCol+1
        indexp4 = i+nbCol+2
        
        p1 = tabPoint[indexp1]          # p1---p2
        p2 = tabPoint[indexp2]          #  |   |
        p3 = tabPoint[indexp3]          # p3---p4
        p4 = tabPoint[indexp4]

        pointAretes = []
        if (tabSigne[indexp1] + tabSigne[indexp2] == 0):
            pointAretes.append(determinePointArete(p1,p2,isoVal))
        if (tabSigne[indexp2] + tabSigne[indexp4] == 0):
            pointAretes.append(determinePointArete(p2,p4,isoVal))
        if (tabSigne[indexp4] + tabSigne[indexp3] == 0):
            pointAretes.append(determinePointArete(p4,p3,isoVal))
        if (tabSigne[indexp3] + tabSigne[indexp1] == 0):
            pointAretes.append(determinePointArete(p3,p1,isoVal))         
            
        if (len(pointAretes) == 2):
            tabSegments.append(Segment(pointAretes[0].x, pointAretes[0].y, pointAretes[1].x, pointAretes[1].y))
        elif (len(pointAretes) == 4):
            moyenne = (p1.val + p2.val + p3.val + p4.val) / 4.0
            if (moyenne >= isoVal):
              tabSegments.append(Segment(pointAretes[0].x, pointAretes[0].y, pointAretes[3].x, pointAretes[3].y))
              tabSegments.append(Segment(pointAretes[1].x, pointAretes[1].y, pointAretes[2].x, pointAretes[2].y))
            else:
              tabSegments.append(Segment(pointAretes[0].x, pointAretes[0].y, pointAretes[1].x, pointAretes[1].y))
              tabSegments.append(Segment(pointAretes[2].x, pointAretes[2].y, pointAretes[3].x, pointAretes[3].y))  
    return tabSegments

def determinePointArete(pt1, pt2, a):
    u = pt1.val
    v = pt2.val
    t = (a-u)/(v-u)
    Xx = ((v-a)/(v-u))*pt1.x + ((a-u)/(v-u))*pt2.x
    Xy = ((v-a)/(v-u))*pt1.y + ((a-u)/(v-u))*pt2.y
    return Point(Xx,Xy,a)

def drawForOneIsoValue(imgFile, data, nbCol, nbRow, isoValue, color):
    signes = determinePlusLess(data, isoValue)
    tabSegment = marchingSquare(data, signes, isoValue, nbCol, nbRow)
    drawPS(imgFile, tabSegment, nbCol, nbRow, color)
    
    
def drawPS(fichier, tabSegment, nbCol, nbRow, color):
#    fichier = file('resultat.ps', 'w')
#    fichier.write("%!PS\n")
#    coefMult = 10
#    drawGrid(fichier, tabPoint, nbCol, nbRow,coefMult)

    fichier.write("0 0 moveto\n")
    fichier.write(color + " setrgbcolor\n")
    large = 500/(max(nbCol,nbRow))
 #  print tabSegment,"len(tabSegment)",len(tabSegment)

    for segId in range(0,len(tabSegment)):
        seg = tabSegment[segId]
        fichier.write(str(int(large*seg.x1)) + " " + str(int(large*seg.y1)) + " moveto\n")
        fichier.write(str(int(large*seg.x2)) + " " + str(int(large*seg.y2)) + " lineto\n")

    fichier.write("stroke\n")
#    fichier.write("stroke\nshowpage")
#    fichier.close()
#    os.system("gs -sDEVICE=jpeg -dJPEGQ=100 -dNOPAUSE -dBATCH -dSAFER -r100x100 -sOutputFile=" +"resultat"+'.jpg '+ "resultat" +'.ps')       
    return
        
        
def drawGrid(fichier, nbCol,nbRow):
#    print  nbCol,nbRow
    large = 500/(max(nbCol,nbRow))
    fichier.write("0 0 0 setrgbcolor\n")
    fichier.write("0 0 moveto\n")
    for i in range(0,nbRow+1):
        fichier.write("0" + " " + str(large*i) + " moveto\n")
        fichier.write(str(large*nbRow) + " " + str(large*i) + " lineto\n")

    fichier.write("0 0 moveto\n")
    for i in range(0,nbCol+1):
        fichier.write( str(large*i) +" "+"0" + " moveto\n")
        fichier.write( str(large*i) + " " + str(large*nbCol) + " lineto\n")

    fichier.write("stroke\n")
    return
    
    
# if __name__ == "__main__":
#     (data, nbCol, nbRow) = lectureData("data.txt")
#     isoValue = 1.5
#     signes = determinePlusLess(data, isoValue)
#     tabSegment = marchingSquare(data, signes, isoValue, nbCol, nbRow)
#     drawPS(data, tabSegment, nbCol, int(nbRow))
#     print "Done !", "nbRow",nbRow,"nbCol",nbCol



