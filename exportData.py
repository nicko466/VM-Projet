import exceptions

# try to get a integer from a string, if not possible a float or then the same string
# @param s: (string)
# @return integer float or string
def try2getInt(s):
    try:
        return int(s)
    except exceptions.ValueError:
        try:
            return float(s)
        except exceptions.ValueError:
		if s == '-':
        		return -1
		else:
			return s

# take a file and parse data in a matrice
# @param  src : the file
# @return a matrice [[]]
def parseData(src):
    mat = []
    for line in src:
	if line != "\n":
		dataLine = line.split("\t")
		for idElt in range(0, len(dataLine)):
			elt = dataLine[idElt]
			dataLine[idElt] = try2getInt(elt)
            	mat.append(dataLine)
    return mat

# return the matrice data
def getMatriceData():
	source = open("donnees_projet/dataVrac.txt", "r")
	return parseData(source)
