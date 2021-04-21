# gitHubapi
# Thank you to : https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8#file-github_api_example-py-L18

import requests, json

github_key = open(file="github_key.txt")
token = github_key.read()
username = 'westbrookmd'

access_token = token
headers = {'Authorization':"Token "+access_token}
gh_session = requests.Session()
gh_session.auth = (username, token)
issues=[]
for page_num in range(1,2):
    try:
        issues_url = f'https://api.github.com/repos/SimCMinMax/WoW-BugTracker/issues?page={page_num}'
        print(issues_url)
        issues = json.loads(gh_session.get(issues_url).text)
        issues.append(issue)
    except:
        issues.append(None)

wow_issues = open("wow_issues.txt", "w")
json.dump(issues, wow_issues)

for issue in range(len(issues)):
    print ("Issue " + str(issue) + " Title: " + str(issues[issue]['title']))

print(len(issues))

exit()
# make more requests using "gh_session" to create repos, list issues, etc.

# loop through all pages to obtain all the repos' information
issues=[]
for page_num in range(1,20):
    try:
    # to find all the repos' names from each page
        url = f"https://github.com/SimCMinMax/WoW-BugTracker/issues?page={page_num}&q=is%3Aissue+is%3Aopen"
        issue = requests.get(url,headers=headers).json()
        issues.append(issue)
    except:
        issues.append(None)


for page in issues:
    if page==[]:
        print(issues.index(page))
        break
# there are 17 pages
print(len(issues))
print(issues)
print(issues[0])
