# GitHib_Treading_Repos
This is a REST microservice that lists the languages used by the 100 trending public repos on GitHub, using Github REST API.
The Python_Github_API fetch data from REST repositories endpoints on Github and decode the data and pass the json response to the function “LanguagesCounter” that finds the list of languages used and counts the number of times it's used. The function “RepoListLanguages” gives the list of repos using every language.
The trending repositories are simply fetched from the most starred repos created in the last 30 days ( from now )
