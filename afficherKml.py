from simplekml import Kml

######################################
############## MAIN ##################
######################################
pathToKML = "KML/"
kml = Kml(name='KmlUsage')
kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])  # A simple Point
kml.save(pathToKML+"KmlClass.kml")  # Saving
kml.savekmz(pathToKML+"KmlClass.kmz", format=False)  # Saving as KMZ
print kml.kml()  # Printing out the kml to screen