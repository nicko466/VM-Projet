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
    kml = Kml(name='KmlUsage')
    ground = kml.newgroundoverlay(name='GroundOverlay')
    #path image
    ground.icon.href = "../"+pathImage
    #Coordonnee pour ajouter l'image
    ground.gxlatlonquad.coords = [(x0,y1),(x1,y1),
                              (x1,y0),(x0,y0)]
    
    kml.save(pathToKML+"KmlClass.kml")  # Saving
    kml.savekmz(pathToKML+"KmlClass.kmz", format=False)  # Saving as KMZ
    print kml.kml()  # Printing out the kml to screen