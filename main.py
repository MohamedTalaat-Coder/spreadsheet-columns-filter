from classes import Excel
import sys


try:
    file = input("File: ").replace('"', '')
    excel = Excel(file)
except:
    sys.exit("File Not Found.")

try:
    for row in excel.show_columns():
        print(row)
except KeyError:
    sys.exit("Invalid Column Name.")