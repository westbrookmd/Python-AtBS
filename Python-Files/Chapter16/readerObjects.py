import csv, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)

#You should not put large csv files into memory at once like this. Instead, use a loop to grab certain parts
exampleData = list(exampleReader)

"""for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))"""

logging.debug(exampleData)

logging.debug(exampleData[0][1]) #[1st row][2nd col]

""" Here is how to use writer Objects"""

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1,2,3.141592,4])
outputFile.close()


""" delimiter and lineterminator Keyword Arguments for writer Objects"""

#import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])

csvWriter.writerow(['eggs', 'bacon', 'ham'])

csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csvFile.close()


""" DictReader and DictWriter CSV Objects. These are used for CSV files that contain heaer rows"""
#import csv
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])


"""If you have a csv file that doesn't have headers, DictReader() has a second argumnet that is used for containing made-up header names below"""
#import csv
exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name','amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])


"""Want to just write a header row instead?"""
#import csv
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'})
outputFile.close()


