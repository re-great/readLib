import json
from libgen_api import LibgenSearch


def GetbyTitle(query):

	s = LibgenSearch()
	results = s.search_title(query)
	return results

def GetbyAuthor(query):

	s = LibgenSearch()
	results = s.search_author(query)
	return results
