import csv
import json

latdict = dict()
longdict = dict()

with open('zipcode.csv', 'rb') as csvfile:
	zipreader = csv.DictReader(csvfile)
	for row in zipreader:
		if row['zip']:
			if int(row['zip']) < 1000:
				cur = '00' + row['zip']
				latdict[cur] = float(row['latitude'])
				longdict[cur] = float(row['longitude'])
			elif int(row['zip']) < 10000:
				cur = '0' + row['zip']
			else:
				cur = row['zip']
			latdict[cur] = float(row['latitude'])
			longdict[cur] = float(row['longitude'])

latlist = []
longlist = []
genderlist = []
cdict = {'latitude': 40.115, 'longitude': -88.27278}
clat = 40.115
clong = -88.27278

with open ('../student_locations.csv', 'rb') as csvfile:
	locreader = csv.DictReader(csvfile, delimiter = ',')

	for row in locreader:

		if row['Nation'] is not ' ':
			continue
		else:
			cur = row['Zip']
			if '-' in cur:
				cur = cur[:cur.index('-')]
		if cur not in latdict:
			continue
		latlist.append(latdict[cur])
		longlist.append(longdict[cur])
		genderlist.append(row['Gender'])

jsondict = []
for i in range(len(latlist)):
	cur = {}
	cur['origin'] = cdict
	ddict = {'latitude': latlist[i], 'longitude': longlist[i]}
	cur['destination'] = ddict

	if genderlist[i] == 'M':
		cur['options'] = {
            'strokeWidth': 2,
            'strokeColor': 'rgba(0, 0, 255, 0.4)'}
	else:
		cur['options'] = {'strokeWidth': 1, 'arcSharpness': 1.4}
	jsondict.append(cur)

print len(jsondict)

with open('result.json', 'w') as fp:
    json.dump(jsondict, fp, indent=4)


