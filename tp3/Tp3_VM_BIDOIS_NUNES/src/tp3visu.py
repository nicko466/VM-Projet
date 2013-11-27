import math
muI= 2 #ou 2

   
def drawChart(dataTab,valeurs, nomFich):
    data =""
    for i in range (0, len(dataTab)):
        data +="['"+str(int(dataTab[i].val))+"', "+str(dataTab[i].x)+', '+str(dataTab[i].y)+", 'Point de base'," + str(dataTab[i].val)+'],\n'
        
    for i in range (0, len(valeurs)):
        data +="['"+str(int(valeurs[i].val))+"', "+str(valeurs[i].x)+', '+str(valeurs[i].y)+", 'Point rajoutes'," + str(valeurs[i].val)+'],\n'
        
    fichier = open(nomFich, 'w') 
    content="""<html><head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Value', 'X', 'Y', 'Type',     'Size'],"""+data+"""]);
        var options = {
          width: 1400,
          height: 900,
          title: 'Visualisation tp-3',
          hAxis: {title: 'X'},
          vAxis: {title: 'Y'},
          bubble: {textStyle: {fontSize: 11}},
        };
        var chart = new google.visualization.BubbleChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>"""
    fichier.write(content)
    
class Point : 
  def __init__(self, x, y,val):
    self.x = float(x)
    self.y = float(y)
    self.val = float(val)
    
  def __repr__(self):
    return "{x: " +str((self.x)) + " y:" + str((self.y)) + " v:" + str (int(self.val))+"}"


def lectureData(fich):
    fichier = open(fich, 'r') 
    tabRes = []
    while True :
        line = fichier.readline()
        if line == '' :
          break
        (ville, x, y, val) = line.split(" ")
        val =(val.split("\n"))[0]
        tabRes.append( Point(x,y, val))
    return tabRes

def norme(point):
    return math.sqrt(point.x * point.x + point.y * point.y)

def distance (pOrig,p2):
    pf = Point( pOrig.x- p2.x, pOrig.y -p2.y,0.0)
    return norme (pf)

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
        
    print "denominateur",denominateur, "numerateur",numerateur, "res:",numerateur/denominateur
    return numerateur/denominateur


def shepard(point,dataTab):
    tabDist = creerTabDistance(dataTab, point) 
    print "tabDist",tabDist
    
    res=0
    for i in range(0,len(dataTab)):
        omega= calculOmega(tabDist,i)
        print "omega: ", omega 
        res+= dataTab[i].val * (omega)
    return res
    
if __name__ == "__main__":
    dataTab = lectureData("data.txt")
    print "dataTab",dataTab
    tabPointGenere= []
    for i in range (1,10):
        x =5.2+ (i/10.0)
        y =45+ (i/12.0)
        
        pt =Point(x,y,0)
        pt.val=shepard(pt,dataTab)
        tabPointGenere.append(pt)
        
        pt =Point(6- (i/10.0),45+ (i/12.0),0)
        pt.val=shepard(pt,dataTab)
        tabPointGenere.append(pt)
 
    pt =Point(5.7,45.2,0)
    pt.val=shepard(pt,dataTab)
    tabPointGenere.append(pt)
    
    pt =Point(5.6,45.1,0)
    pt.val=shepard(pt,dataTab)
    tabPointGenere.append(pt)       
    print tabPointGenere
    drawChart(dataTab,tabPointGenere, "chart.html")
    