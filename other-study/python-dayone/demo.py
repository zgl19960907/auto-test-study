import openpyxl


workbook = openpyxl.load_workbook('case.xlsx')
sheet = workbook['Sheet1']
print(str(sheet['id']))