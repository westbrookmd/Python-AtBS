import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

#Create the chart
chartObj = openpyxl.chart.BarChart()


#Get data and labels from the worksheet through references
labels = openpyxl.chart.Reference(sheet, min_col = 1, min_row = 2, max_row = 15)
data = openpyxl.chart.Reference(sheet, min_col = 2, min_row = 2, max_row = 15)

#Add the data and labels (by set_categories)
chartObj.add_data(data, titles_from_data = True)
chartObj.set_categories(labels)

#Chart Formatting
chartObj.title = 'Produce Data'
chartObj.x_axis.title = 'Produce'
chartObj.y_axis.title = 'Quantity'

sheet.add_chart(chartObj, 'F5')
wb.save('sampleChart.xlsx')
