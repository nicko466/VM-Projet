import os
import math
# 
#
#
nbVal = 256

def construction(moyenne,details):
    tableau=[]
    for i in range(0,len(moyenne)):
        tableau.append(moyenne[i] + details[i] )
        tableau.append(moyenne[i] - details[i] )        
    
    return tableau

def constructAll(moyenneInit, collectionDetails):
    tabMoyenneTotal = []
    currentMoyennes = moyenneInit
    index = len(collectionDetails) -1
    #print (index)
    while index >= 0:
      currentMoyennes = construction(currentMoyennes, collectionDetails[index])
      index = index - 1
    return currentMoyennes


def decomposition(tableau,coefMinimal):
    details= []
    moyennes= []
    
    if len(tableau)==1:
        return (tableau, 0)

    else:
        i=0
        while i < len(tableau):
            moy=(tableau[i] +tableau[i+1] )/2
            det=(tableau[i] -tableau[i+1] )/2
            i=i+2
            if math.fabs(det)<coefMinimal:
                details.append(0)
            else :
                details.append(det)    
            moyennes.append(moy)
    return (moyennes, details)


def decompositionAll (tabO,coefMinimal):
    tabMoy= tabO
    colDet =[]
    #nstep = math.log(len(tabO))/math.log(2)
    #print (nstep)
    index = 0
    while len(tabMoy) > 4:
	print len(tabMoy)
        #(moy,det)= decomposition(tabMoy,coefMinimal)
        (moy,det)= decomposeCourbe(tabMoy,coefMinimal)
        colDet.append(det)
        tabMoy= moy
        index = index + 1
    return (tabMoy, colDet)


def genererCourbe():
    tab= []
    for i in range(1,nbVal+1):
        logi=math.log(i)
        tab.append(logi)
    return tab

def compareMax(tab1,tab2):
    tauxErr= 0
    if len(tab1)!=len(tab2):
        return False
    else:
        for i in range(0, len(tab1)):
            if math.fabs(tab1[i]-tab2[i]) > tauxErr:
                tauxErr=math.fabs(tab1[i]-tab2[i])
    return tauxErr

def compareSommme(tab1,tab2):
    tauxErr= 0
    if len(tab1)!=len(tab2):
        return False
    else:
        for i in range(0, len(tab1)):
            tauxErr += math.fabs(tab1[i]-tab2[i]);
    return tauxErr

def courbeDifferenceCompareSomme(imageInitialise,parametreBegin,parametreEnd,step):
    parametreX = []
    ErreurY = []
    tabAfterReconstruction = []
    parametre = parametreBegin
    while parametre < parametreEnd:
        (moyenneDegrade, colDet) = decompositionAll(imageInitialise,parametre)
        tabAfterReconstruction = constructAll(moyenneDegrade,colDet)
        parametreX.append(parametre)
        ErreurY.append(compareSommme(tabAfterReconstruction,imageInitialise))
        parametre += step
    return (parametreX,ErreurY)

def courbeDifferenceCompareMax(imageInitialise,parametreBegin,parametreEnd,step):
    parametreX = []
    ErreurY = []
    tabAfterReconstruction = []
    parametre = parametreBegin
    while parametre < parametreEnd:
        (moyenneDegrade, colDet) = decompositionAll(imageInitialise,parametre)
        tabAfterReconstruction = constructAll(moyenneDegrade,colDet)
        parametreX.append(parametre)
        ErreurY.append(compareMax(tabAfterReconstruction,imageInitialise))
        parametre += step
    return (parametreX,ErreurY)

def afficherCourbe(tabX,tabY):
    fichier = file('test.txt','w')
    for i in range(0,len(tabX)) :
        fichier.write("%f %f\n"%(tabX[i],tabY[i]))
    fichier.close()
    #os.system("cd /home/nicko2/Documents/RICM5/VM/TP")
    #os.system("gnuplot")
    #os.system("plot 'test.txt' ")

class Point : 
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __repr__(self):
    return str(self.x) + " " + str(self.y)

def decomposeCourbe(tableau,coefMinimal):
    details= []
    moyennes= []
    n = len(tableau)
    if len(tableau)==4:
        return (tableau, 0)

    else:
        i=0
        while i < len(tableau):

            imoins2 = (i-2) % n
            imoins1 = (i-1) % n
            iplus1 = (i+1) % n
            
            moy = Point(
            ((1.0/4.0)*(-tableau[imoins2].x + 3*tableau[imoins1].x + 3*tableau[i].x - tableau[iplus1].x)),
            ((1.0/4.0)*(-tableau[imoins2].y + 3*tableau[imoins1].y + 3*tableau[i].y - tableau[iplus1].y)))
            det = Point(
            (1.0/4.0)*(tableau[imoins2].x - 3*tableau[imoins1].x + 3*tableau[i].x - tableau[iplus1].x),
            (1.0/4.0)*(tableau[imoins2].y - 3*tableau[imoins1].y + 3*tableau[i].y - tableau[iplus1].y))
           
            i=i+2
            #print det.x,det.y
            detNorm = math.sqrt(det.x * det.x + det.y * det.y)
            #print detNorm
            if math.fabs(detNorm)<coefMinimal:
                details.append(0)
            else :
                details.append(det)    
            moyennes.append(moy)
    return (moyennes, details)


def dessinerCourbePS(tableau):
    fichier = file('courbesDecomp.ps','w')
    fichier.write("%!PS\n1 0 0 setrgbcolor\n")
    coefMulti = 50
    premierX = tableau[0].x*coefMulti
    premierY = tableau[0].y*coefMulti
    fichier.write(str(premierX)+ " " + str(premierY) + " moveto\n")
    for i in range(1,len(tableau)) :
        fichier.write("%s %s lineto\n"%(str(tableau[i].x*coefMulti),str(tableau[i].y*coefMulti)))
    fichier.write(str(premierX)+ " " + str(premierY) + " lineto\n")
    fichier.write("stroke\nshowpage")
    fichier.close()
    
def lireCourbe(nomCourbe):
  fichier = open(nomCourbe,'r') 
  tableauX = []
  tableauY = []
  while True :
    line = fichier.readline()
    
    if line == '' :
      break;
    else :
      (x,y) = line.split(" ")
      y = y.split("\r")[0]
      tableauX.append(float(x))
      tableauY.append(float(y))
  return (tableauX,tableauY)
    
    
def constructPointTable(tabX, tabY):
  tabRes = []
  for i in range (0,len(tabX)):
    tabRes.append(Point(tabX[i],tabY[i]))
  return tabRes

if __name__ == "__main__":
  (tableauX,tableauY) = lireCourbe("crocodile.txt")
  #tabPoint = constructPointTable(tableauX,tableauY)
  #dessinerCourbePS(tabPoint)
  coefMinimal = 0.2
  tabPoint = constructPointTable(tableauX,tableauY)
  #(moy, det) = decomposeCourbe(tabPoint,coefMinimal)
  (moy, det) = decompositionAll(tabPoint,coefMinimal)
  print moy
  dessinerCourbePS(moy)
  
  