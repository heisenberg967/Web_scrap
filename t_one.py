import glob
import xlrd
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xlfiles=glob.glob('D:/Work/Datascience Intern/*.xlsx')

wf = csv.writer(open('D:/Work/Datascience Intern/one.csv','wb'),delimiter=',')

for files in xlfiles:
	#print files
	workbook = xlrd.open_workbook(files)
	sheet = workbook.sheet_by_index(0)
	for row in range(1,sheet.nrows):
		#print sheet.row_values(row)
		wf.writerow(sheet.row_values(row))
