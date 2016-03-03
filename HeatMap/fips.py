import csv
import json

zipdict = dict()
with open('zip_county.csv', 'rb') as csvfile:
	zipreader = csv.DictReader(csvfile)
	for row in zipreader:
		zipCode = row['ZIP']
		fipsCode = row['COUNTY']
		zipdict[zipCode] = fipsCode

fipsCount = dict ()
total = 0.00
for cur in zipdict.itervalues():
	fipsCount[cur] = 0.01


with open ('../student_locations.csv', 'rb') as csvfile:
	locreader = csv.DictReader(csvfile, delimiter = ',')

	for row in locreader:

		if row['Nation'] is not ' ':
			continue
		else:
			cur = row['Zip']
			if '-' in cur:
				cur = cur[:cur.index('-')]
		if cur not in zipdict:
			print "NO fip code for this zip:", cur
			continue
		fipCode = zipdict[cur]
		fipsCount[fipCode] += 1

writer = csv.writer(open('result.tsv', 'wb'))
writer.writerow(["id","rate"])
max = 0.00
for key, value in fipsCount.items():
	writer.writerow([key, value])
	if (float(value) > max):
		max = float(value)
print max



