import xlrd
import json
import csv
import heapq

#----------------------------------------------------------------------
def get_class_info(path):
	book = xlrd.open_workbook(path)
	data = book.sheet_by_index(2)
	female_count = {}
	total_count = {}
	for row_idx in range(1, data.nrows):
		name = str(data.row_values(row_idx)[2])
		num = name.split(" ")[1]
		if int(num) < 125 or int(num) == 498 or int(num)==598:
			continue
		gender = str(data.row_values(row_idx)[3])
		if name not in female_count:
			female_count[name] = 0
			total_count[name] = 0
		if gender == 'F':
			female_count[name] += float(data.row_values(row_idx)[4])
		total_count[name] += float(data.row_values(row_idx)[4])

	class_percentage = {}
	for cur in female_count:
		class_percentage[cur] = female_count[cur]/total_count[cur]
	res_key = heapq.nlargest(20 ,class_percentage, key = lambda k: class_percentage[k])

	res_list = []
	res_percentage = []
	for cur in res_key:
		res_list.append(cur)
		res_percentage.append(class_percentage[cur])
	print res_list, "\n",res_percentage
	


			

if __name__ == "__main__":
    path = "../gender10_enrollment.xlsx"
    get_class_info(path)
