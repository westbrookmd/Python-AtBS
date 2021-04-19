import ezsheets, logging, openpyxl
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

sheet_name = input("Input the digits after 'docs.google.com/spreadsheets/d/': " )
# Example sheet 1JCVnNPNvjvecRMULcCNffGjbYFKb7Are0DvQcaS7G_A (private)
ss = ezsheets.Spreadsheet(sheet_name)
#Get Title
logging.debug(ss.title)

#Sheet objects in order
logging.debug(ss.sheets)

#Delete sheet object
#del ss[0]


#Download file
#ss.downloadAsExcel()
#ss.downloadAsExcel('a_different_filename.xlsx')
#ss.delete() # Delete the spreadsheet.

#ezsheets.listSpreadsheets() #Get all of the sheets on the account

# sheet.refresh() #refresh the local data in the sheet object


""" Start pyxl stuff here..."""
#ss.downloadAsExcel()
ss.downloadAsExcel('barChartSheet.xlsx')
wb = openpyxl.load_workbook('barChartSheet.xlsx')
sheet = wb['Sheet1']

chartObj = openpyxl.chart.BarChart()

labels = openpyxl.chart.Reference(sheet, min_col = 1, min_row = 2, max_row = 5)
data = openpyxl.chart.Reference(sheet, min_col = 2, min_row = 2, max_row = 5)

#Add the data and labels (by set_categories)
chartObj.add_data(data, titles_from_data = True)
chartObj.set_categories(labels)

#Chart Formatting
chartObj.title = 'Quick Start'
chartObj.x_axis.title = 'Quick'
chartObj.y_axis.title = 'Start'

sheet.add_chart(chartObj, 'F5')
wb.save('barChartSheet.xlsx')

ss = ezsheets.upload('1JCVnNPNvjvecRMULcCNffGjbYFKb7Are0DvQcaS7G_A')
