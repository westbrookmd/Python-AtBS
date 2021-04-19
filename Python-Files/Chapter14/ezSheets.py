import ezsheets


ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]

sheet.getRow(1)

columnOne = sheet.getColumn(1)
sheet.getColumn(1)

rows = sheet.getRows()
rows[0] #examine values in the first rows
#rows[1][0] = 'PUMPKIN' #Changes the produce name (Change the second row, first item to ...

#sheet.updateRows(rows) #Update the online spreadsheet

#sheet.columnCount #this is the number of columns in the sheet
#sheet.columnCount = 100 #This changes the number of columns, deleting any outside this range

#ss.createSheet('NewSheet')
#ss.createSheet('Bacon', 0) #new sheet at index 0

#ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
#ss[0].copyTo(ss2) # Copy the ss's Sheet1 to the ss2 spreadsheet.

