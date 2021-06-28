from openpyxl import *

wb = load_workbook("ExcelTesting.xlsx")
xl = wb.active
# wb.save("ExcelTesting.xlsx")
#
# # print(xl["C2"].value)
#
# aa=xl["C4"].value
# print(aa.upper())
# print(aa.lower())

xl["J8"] = "test"
wb.save("ExcelTesting.xlsx")