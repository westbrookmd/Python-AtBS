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

Trapper = sum('Trapper' in s for s in titles)

Wraith = sum('Wraith' in s for s in titles)
Hillbilly = sum('Billy' in s for s in titles)
Nurse = sum('Nurse' in s for s in titles)
Myers = sum('Myers' in s for s in titles)
Hag = sum('Hag' in s for s in titles)
Doctor = sum('Doc' in s for s in titles)
Huntress = sum('Hunt' in s for s in titles)
Cannibal = sum('Cannibal' in s for s in titles)
Nightmare = sum('Fred' in s for s in titles)
Pig = sum('Pig' in s for s in titles)
Clown = sum('Clown' in s for s in titles)
Spirit = sum('Spirit' in s for s in titles)
Legion = sum('Legion' in s for s in titles)
Plague = sum('Plague' in s for s in titles)
GhostFace = sum('Ghost' in s for s in titles)
Demogorgon = sum('Demo' in s for s in titles)
Oni = sum('Oni' in s for s in titles)
Deathslinger = sum('Deathslinger' in s for s in titles)
PyramidHead = sum('Pyramid' in s for s in titles)
Blight = sum('Blight' in s for s in titles)
Twins = sum('Twins' in s for s in titles)
Trickster = sum('Trickster' in s for s in titles)

endSentence = " times in the top " + str(len(titles)) + " titles of /r/deadbydaylight of all time!"
endSentence = " "
print("Myers is listed " + str(Myers) + endSentence)
print("Wraith is listed " + str(Wraith) + endSentence)
print("Hillbilly is listed " + str(Hillbilly) + endSentence)
print("Nurse is listed " + str(Nurse) + endSentence)
print("Hag is listed " + str(Hag) + endSentence)
print("Doctor is listed " + str(Doctor) + endSentence)
print("Huntress is listed " + str(Huntress) + endSentence)
print("Cannibal is listed " + str(Cannibal) + endSentence)
print("Pig is listed " + str(Pig) + endSentence)
print("Clown is listed " + str(Clown) + endSentence)
print("Spirit is listed " + str(Spirit) + endSentence)
print("Legion is listed " + str(Legion) + endSentence)
print("Plague is listed " + str(Plague) + endSentence)
print("Ghostface is listed " + str(GhostFace) + endSentence)
print("Demogorgon is listed " + str(Demogorgon) + endSentence)
print("Oni is listed " + str(Oni) + endSentence)
print("Deathslinger is listed " + str(Deathslinger) + endSentence)
print("Pyramidhead is listed " + str(PyramidHead) + endSentence)
print("Blight is listed " + str(Blight) + endSentence)
print("Twins is listed " + str(Twins) + endSentence)
print("Trickster is listed " + str(Trickster) + endSentence)





