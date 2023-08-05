#.KML to .plan converter
#NMark

class Item:

	def __init__(self, Altitude, Command, Lon, Lat, last = 0, DoJumpId = 1, AltitudeMode = 1, autoContinue = 'true', Frame = 3, AMSLAltAboveTerrain = 'null'):
		self.Altitude = Altitude
		self.Command = Command
		self.Lon = Lon
		self.Lat = Lat
		self.DoJumpId = DoJumpId
		self.AltitudeMode = AltitudeMode
		self.autoContinue = autoContinue
		self.Frame = Frame
		self.AMSLAltAboveTerrain = AMSLAltAboveTerrain
		self.last = last

	def __str__(self):
		front = "{\n"
		string = f'\t\t\"AMSLAltAboveTerrain\": {self.AMSLAltAboveTerrain},\n\
		\"Altitude\": {self.Altitude},\n\
		\"AltitudeMode\": {self.AltitudeMode},\n\
		\"autoContinue\": {self.autoContinue},\n\
		\"command\": {self.Command},\n\
		\"doJumpId\": {self.DoJumpId},\n\
		\"frame\": {self.Frame},\n\
		\"params\": [\n\
		   15,\n\
		   0,\n\
		   0,\n\
		   0,\n\
		   {self.Lat},\n\
		   {self.Lon},\n\
		   50\n\
		],\n\
		\"type\": \"SimpleItem\"\n'

		if self.lest = 0:
			back = "},\n"
		if self.last = 1:
			back = "}\n"
	
		return front+string+back

class Point:

	def __init__(self, Altitude, Lon, Lat, Order, Name = 'point'):
		self.Altitude = Altitude
		self.Lon = Lon
		self.Lat = Lat
		self.Order = Order
		self.Name = Name

	def __repr__(self):
		return f'{self.Lon},{self.Lat},{self.Altitude},{self.Order},{self.Name}'

def fillPoints(file, points):
	with open(file) as f:
		lines = f.readlines()
	indicator = 0
	count = 1
	for line in lines:
		if indicator < 2:
			if line == '\t\t\t\t</coordinates>\n':
				indicator = 0
			if line == '\t\t\t<Point>\n':
				indicator == 3
			if indicator == 1:
				lineData = line.split()
				for data in lineData:
					value = data.split(',')
					points.append(Point(value[2],value[0],value[1],count))
					count+=1
			if line == '\t\t\t\t<coordinates>\n':
				indicator = 1
		elif indicator == 2:
			split1 = line.split('>')
			split2 = split1[1].split('<')
			data = split2[0].split(',')
			points.append(Point(data[2],data[0],data[1],count))
			count+=1
			indicator = 0
		elif indicator == 3:
			indicator -= 1

def pointToItem(point, command):
	if(point.Order == )
	item = Item(point.Altitude, command, point.Lon, point.Lat, point.Order)
	return item


header = '{\n\
    "fileType": "Plan",\n\
    "geoFence": {\n\
        "circles": [\n\
        ],\n\
        "polygons": [\n\
        ],\n\
        "version": 2\n\
    },\n\
    "groundStation": "QGroundControl",\n\
    "mission": {\n\
        "cruiseSpeed": 15,\n\
        "firmwareType": 12,\n\
        "globalPlanAltitudeMode": 1,\n\
        "hoverSpeed": 5,\n\
        "items": [\n\n'

footer = '\n ],\n\
        "plannedHomePosition": [\n\
            39.94177141,\n\
            -83.21179948,\n\
            279.37707600001795\n\
        ],\n\
        "vehicleType": 1,\n\
        "version": 2\n\
    },\n\
    "rallyPoints": {\n\
        "points": [\n\
        ],\n\
        "version": 2\n\
    },\n\
    "version": 1\n\
}'

infile = 'test1.kml'
outfile = 'test1.plan'
points = []

f = open(outfile, 'w')
f.write(header)
fillPoints(infile, points)
for point in points:
	temp = (pointToItem(point, 16).__str__())
	f.write(temp)

f.write(footer)

f.close()

#print(header)
#fillPoints(infile, points)
#for point in points:
#	print(pointToItem(point, 16))
#print(footer)

