import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print("Time to read the Rows.")
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Check sure state key exists
    countyData.setdefault(state, {})
    # Check key for county in state  exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row = one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Incrase county pop by pop in census tract
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
