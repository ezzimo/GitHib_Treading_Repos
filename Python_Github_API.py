import json, sys, requests
from collections import Counter, defaultdict
from datetime import datetime, timedelta, date
from tabulate import tabulate
from LanguagesRepoCounter import languages_counter
from RepoListLanguages import groupby_language

def get_data():
    one_month_ago = datetime.date(datetime.now()) - timedelta(days=30)
    url = "https://api.github.com/search/repositories"
    params = {"q": f">{one_month_ago.isoformat()}",
              "sort": "stars",
              "order": "desc",
              "page": 1,
              "per_page": 100}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["items"]

def groupby(values, key):
    grouped = defaultdict(list)
    for x in values:
        grouped[x[key]].append(x)
    return grouped
grouped_repos = groupby(get_data(), "language")

#Counting the number of repo using every language
counts = {language: len(repos) for language, repos in grouped_repos.items()}

urls = {language: [repo["html_url"] for repo in repos]
        for language, repos in grouped_repos.items()}

# Displaye the repo's urls for every language
for key in urls:
	print(key, ' language used in')
	for i in range(len(urls[key])):
    #for language, repos in grouped_repos.items()
		print("                           ", urls[key][i])


# Displaye the number of repos using every language in a table
table = []
for key in counts:
	under_table=[]
	under_table.append(key)
	under_table.append(counts[key])
	table.append(under_table)
print(tabulate(table, headers=('Language', 'number of Repo using it'), tablefmt="grid"))
