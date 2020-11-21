def LanguagesCounter(Data):
	''' Count how many times every programming language is used in the 100 most starred repos created in the last 30 days given in a parameter as json object, return a dict with languages as a keys and number of repo using this language as a value
	'''
	Languages_liste = []
	for i in range(len(Data["items"])):
		Languages_liste.append(Data["items"][i]["language"])
	Lang_Dic_Count ={i:Languages_liste.count(i) for i in Languages_liste}
	return Lang_Dic_Count
