import json, openpyxl

with open('wow_issues.json') as json_file:
    wowData = json.load(json_file)
#wowfile = open('wow_issues.json')
#wowData = wowfile.read()
#print(wowData)
#for issue in range(len(wowData)-1):
#    print ("Issue " + str(issue) + " Title: " + str(wowData[issue]))
print(type(wowData))
#for issue in range(len(wowData)):
#    print ("Issue " + str(issue) + " Title: " + str(wowData[issue]['title']))
