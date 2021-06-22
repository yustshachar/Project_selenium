from openpyxl import *

xl = load_workbook("ExcelTesting.xlsx").active

# print(xl["C2"].value)

aa=xl["C4"].value
print(aa.upper())
print(aa.lower())