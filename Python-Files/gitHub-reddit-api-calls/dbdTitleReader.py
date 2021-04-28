import json, openpyxl

with open('dbdTitlesRaw.json') as json_file:
    dbdTitles = json.load(json_file)
#wowfile = open('wow_issues.json')
#wowData = wowfile.read()
#print(wowData)
#for issue in range(len(wowData)-1):
#    print ("Issue " + str(issue) + " Title: " + str(wowData[issue]))
print(type(dbdTitles))
#for issue in range(len(wowData)):
#    print ("Issue " + str(issue) + " Title: " + str(wowData[issue]['title']))



titles = []
dbdTitlesUnclassified = 0
#print(dbdTitles['data']['children'][0]['data']['title'])

for i in range(len(dbdTitles['data']['children'])):
    #try:
    titles.append(dbdTitles['data']['children'][i]['data']['title'])
    #except:
    #dbdTitlesUnclassified += 1

print(titles)
#dbdTitlesFile = open("dbdTitles.json", "w")
#json.dump(titles, dbdTitlesFile)

Myers = sum('Myers' in s for s in titles)
endSentence = " times in the top " + str(len(titles)) + " titles of /r/deadbydaylight of all time!"
print("Myers is listed " + str(Myers) + endSentence)





