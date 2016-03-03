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


with open ('test.tsv', 'rb') as csvfile:
	locreader = csv.DictReader(csvfile, delimiter = '\t')
	for row in locreader:
		fipsCount[int(row['id'])] = 0.01

with open ('../student_locations.csv', 'rb') as csvfile:
	locreader = csv.DictReader(csvfile, delimiter = ',')

	for row in locreader:

		if row['Nation'] is not ' ':
			continue
		else:
			cur = row['Zip']
			if '-' in cur:
				cur = cur[:cur.index('-')]
		fipCode = zipdict[cur]
		if (int(fipCode) < 10000):
			fipCode = fipCode[1:]
		if cur not in zipdict:
			print "NO fip code for this zip:", cur
			continue
		if fipCode not in fipsCount:
			fipsCount[int(fipCode)] = 0.01
		fipsCount[int(fipCode)] += 1

with open("result.tsv", "w") as record_file:
    record_file.write("id\trate\n")
    for key in sorted(fipsCount.iterkeys()):
        record_file.write(str(key)+"\t"+str(fipsCount[key])+"\n")



