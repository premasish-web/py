from fuzzywuzzy import fuzz
from fuzzywuzzy import process
with open("positive.txt")as f:
    positive=f.read().split("/n")
    len(positive)
    from fuzzywuzzy import process
    def get_matches(query,choices,limit=3):
    results = process.extract(query,choices,limit=limit)
    return results
get_matches("good",positive)
