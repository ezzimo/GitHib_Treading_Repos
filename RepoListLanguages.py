def RepoListLanguages(Data, list):
	'''
	return the list of repositories from Data parameter for every programming language in the list parameter as a dictionary with the programming language as key and a list of repositories as value
	'''
	languagesRepo = {}
	for key in list:
		languagesRepo[key]= []
		for repo in range(len(Data["items"])):
			if (key == Data["items"][repo]["language"]):
				languagesRepo[key].append(Data["items"][repo]["html_url"])

	return languagesRepo
