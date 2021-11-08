# search_title()
import json
from libgen_api import LibgenSearch

s = LibgenSearch()
print("")
p = input("Search by title \n: Input title  :  ")

# results = s.search_author(p)
results = s.search_title("Pride and Prejudice")
print(json.dumps(results, indent=2))
