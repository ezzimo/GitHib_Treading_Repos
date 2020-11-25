from collections import Counter

def languages_counter(data):
    ''' Count how many times every programming language is used given in a parameter as json object, return a dict with languages as a keys and number of repo using this language as a value
    '''
    return Counter(repo["language"] for repo in data["items"])
