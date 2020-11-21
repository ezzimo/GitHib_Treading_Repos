import urllib.request, urllib.parse, urllib.error
import json
from collections import Counter
from datetime import datetime, timedelta, date
from LanguagesRepoCounter import LanguagesCounter
from RepoListLanguages import RepoListLanguages
from tabulate import tabulate


One_Mouth_ago_date = datetime.date(datetime.now()) - timedelta(days=30)

url = 'https://api.github.com/search/repositories?q=created:%3E'+One_Mouth_ago_date.isoformat()+'&sort=stars&order=desc&page=1&per_page=100'

data_connection_request  = urllib.request.urlopen(url)

unicoded_data = data_connection_request.read().decode()

try:
	json_data = json.loads(unicoded_data)
except:
	json_data = None

if not json_data or json_data["total_count"]<1:
	print('######## Failure To Retrieve ########')
	print(json_data)



Lang_Dic_Count = LanguagesCounter(json_data)

DicDataList = RepoListLanguages(json_data, Lang_Dic_Count)
for key in DicDataList:
	print(key, ' language used in')
	for i in range(len(DicDataList[key])):
		print("                           ", DicDataList[key][i])

table = []
for key in Lang_Dic_Count:
	under_table=[]
	under_table.append(key)
	under_table.append(Lang_Dic_Count[key])
	table.append(under_table)
print(tabulate(table, headers=('Language', 'number of Repo using it'), tablefmt="grid"))
