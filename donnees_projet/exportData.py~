import exceptions

def try2getInt(s):
    try:
        return int(s)
    except exceptions.ValueError:
        try:
            return float(s)
        except exceptions.ValueError:
            return s



def filtrer(src):
    """Fonction de traitement.
    Lit et traite ligne par ligne le fichier source (src). 
    """
    mat = []
    for line in src:
	if line != "\n":
		dataLine = line.split("\t")
		for idElt in range(0, len(dataLine)):
			elt = dataLine[idElt]
			dataLine[idElt] = try2getInt(elt)
            	mat.append(dataLine)
	
    return mat



source = open("dataVrac.txt", "r")
print "result", filtrer(source)
