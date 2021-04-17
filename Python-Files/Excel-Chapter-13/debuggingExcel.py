import logging
import openpyxl
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')
wb = openpyxl.load_workbook('example.xlsx')
#Print worksheet names
logging.debug("List of Sheet Titles = " + str(wb.sheetnames))
#Get a sheet
sheet = wb['Sheet1']
logging.debug("Sheet = " + str(sheet))
#Get a cell from a sheet
cell = sheet['A1']
logging.debug("Cell = " + str(cell))
#Get the cell value
logging.debug("Cell Value = " + str(cell.value))

#each
logging.debug('Row %s, Column %s is %s' % (cell.row, cell.column, cell.value))
