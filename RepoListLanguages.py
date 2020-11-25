from collections import defaultdict

def groupby_language(data):
    '''
    return the list of repositories from data parameter for every programming language as a dictionary with the programming language as key and a list of repositories as value
    '''
    repo_urls = defaultdict(list)
    for repo in data["items"]:
        repo_urls[repo["language"]].append(repo["html_url"])
    return repo_urls
