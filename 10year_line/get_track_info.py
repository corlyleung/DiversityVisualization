import xlrd
import json
import csv

NUM_SHEETS = 9

software_foundations = {422, 426, 427, 428,429, 476, 477, 492, 493, 494, 522, 524, 526, 527, 528, 576, 598}
models_comp = {413, 473, 475, 476, 477, 481, 482, 571, 572, 573, 574, 575, 576, 579, 583, 584}
big_data = {410, 411, 412, 414, 440, 443, 445, 446, 447, 466, 467, 510, 511, 512, 543, 544, 546, 548, 566, 576}
hci = {416, 460, 461,463, 465, 467, 468, 563, 565}
media = {414, 418, 419, 445, 465, 467, 519, 565}
high_performance = {419, 450, 457, 466, 482, 483, 484, 519, 554, 555, 556, 558}
distributed = {423, 424, 425, 431, 436, 438, 439, 460, 461, 463, 483, 484, 523, 524, 525, 538, 563}
machine = {423, 424, 426, 431, 433, 484, 523, 526, 533, 536, 541, 584}

cat_dict = {"software_foundations":software_foundations, "models_comp":models_comp,"big_data":big_data, "hci":hci, "media":media, "high_performance":high_performance, "distributed":distributed, "machine":machine}
percentage = {"software_foundations":[], "models_comp":[],"big_data":[], "hci":[], "media":[], "high_performance":[], "distributed":[], "machine":[]}

#----------------------------------------------------------------------
def get_line_json(path):
	book = xlrd.open_workbook(path)
	for cur_sheet_idx in range(NUM_SHEETS):
		female_count = {"software_foundations":0, "models_comp":0,"big_data":0, "hci":0, "media":0, "high_performance":0, "distributed":0, "machine":0}
		total = {"software_foundations":0, "models_comp":0,"big_data":0, "hci":0, "media":0, "high_performance":0, "distributed":0, "machine":0}
		cur_sheet = book.sheet_by_index(cur_sheet_idx)
		for row_idx in range(2, cur_sheet.nrows-1):
			name = int(str(cur_sheet.row_values(row_idx)[0]).split(" ")[1])
			for cat in cat_dict:
				if name in cat_dict[cat]:
					female_count[cat] += float(str(cur_sheet.row_values(row_idx)[1]))
					total[cat] += float(str(cur_sheet.row_values(row_idx)[3]))
		for cat in cat_dict:
			percentage[cat].append(female_count[cat]/total[cat])

	ave_percentage = {"software_foundations":[], "models_comp":[],"big_data":[], "hci":[], "media":[], "high_performance":[], "distributed":[], "machine":[]}
	for cat in percentage:
		prev = percentage[cat][0]
		for cur in range(1,len(percentage[cat])):
			next = percentage[cat][cur]
			ave = (prev + next)/2
			ave_percentage[cat].append(ave)
			prev=next
	labels = book.sheet_names()[1:9]
	
	for label_idx in range(len(labels)):
		labels[label_idx] = str(labels[label_idx])


	with open('line.csv', 'wb') as csvfile:
		header = ['Label'] + ave_percentage.keys()
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(header)
		for idx in range(len(labels)):
			writer.writerow([labels[idx], ave_percentage["machine"][idx], ave_percentage["big_data"][idx], ave_percentage["high_performance"][idx], ave_percentage["distributed"][idx], ave_percentage["media"][idx], ave_percentage["hci"][idx], ave_percentage["software_foundations"][idx], ave_percentage["models_comp"][idx]])

if __name__ == "__main__":
    path = "../end_enrollment.xlsx"
    get_line_json(path)
