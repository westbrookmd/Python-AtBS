import ezsheets
import logging
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

