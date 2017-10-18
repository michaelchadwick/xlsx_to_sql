#-*- coding: utf-8 -*-
import xlrd
#import csv
from os import sys

#example of sql query template:
TEMPLATE = 'INSERT INTO {0} (col1, col2, col3, col4, col5) VALUES ("{1}", "{2}", "{3}", "{4}", "{5}");\n';

def convert(excel_file, table_name=""):
  try:
    excel = xlrd.open_workbook(excel_file)
  except:
    print 'error: file {0} not found ;('.format(excel_file)
    exit(0)

  all_sheets = excel.sheet_names()
  for sheet_name in all_sheets:
    sheet = excel.sheet_by_name(sheet_name)

    sql_name = table_name if len(table_name) > 0 else sheet_name

    my_sql = open(''.join([sql_name, '.sql']), 'w+')

    #my_csv = open(''.join([sheet_name, '.csv']), 'wb')
    #writer = csv.writer(my_csv, quoting=csv.QUOTE_ALL)

    for row in xrange(sheet.nrows):
      items = []
      for a in sheet.row_values(row):
        items.append(unicode(a).encode('utf-8'))
      #print TEMPLATE_TABLE_1.format(items[0], items[1], items[2])
      my_sql.write(TEMPLATE.format(sql_name, items[0], items[1], items[2], items[3], items[4]))
      #writer.writerow([unicode(entry).encode("utf-8") for entry in sheet.row_values(row)])
    #my_csv.close()
    my_sql.close()

if __name__ == '__main__':
  if len(sys.argv) == 3:
    convert(sys.argv[1], sys.argv[2])
  elif len(sys.argv) == 2:
    convert(sys.argv[1])
  elif len(sys.argv) == 1:
    print 'error: missing excel file'
  else:
    print 'error: wrong number of arguments'
