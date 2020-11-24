# GitHib_Treading_Repos
This is a REST microservice that lists the languages used by the 100 trending public repos on GitHub, using Github REST API.
### Description:
The **Python_Github_API** fetch data from REST repositories endpoints on Github and decode the data and pass the *json* response to the function “**LanguagesCounter**” that finds the list of languages used and counts the number of times it's used. The function “**RepoListLanguages**” gives the list of repos using every language.
The trending repositories are simply fetched from the most starred repos created in the last 30 days ( from now ).<br/>
Requirements are :<br/>
Python 3<br/>
Install python tabulate module ([see](https://pypi.org/project/tabulate/)).

### The query parameters:
 The Search API helps us search for the specific item we want to find. For example, in this program I'm searching for repositories using a specific criteria which is the most starred repositories. It's similar to performing a search on Google. This method returns up to 100 results per page, in this program I'm considering only the first page (but you can specify the page you want in the query).
 for more information on how to use GitHub search API see this [link](https://docs.github.com/en/free-pro-team@latest/rest/reference/search#search-repositories)
 ### Execution:
Download the three files in the same folder.<br/>
in the command line:<br/>
`python3 Python_Github_API.py`
