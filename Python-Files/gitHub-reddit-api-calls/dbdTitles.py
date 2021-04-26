
import requests, json


gh_session = requests.Session()

titles = []
#Careful running this script. It produces 2.3m characters (all from a json api call to reddit)



#Uncomment all lines to run
#titles_url = 'https://www.reddit.com/r/deadbydaylight/top.json?sort=top&t=all&limit=100'
#titles = json.loads(requests.get('https://www.reddit.com/r/deadbydaylight/top.json?sort=top&t=all&limit=100', headers = {'User-agent': 'your bot 0.1'}).text)

#dbdTitlesJson = open("dbdTitles.json", "w")
#json.dump(titles, dbdTitlesJson)
print("Done.")
