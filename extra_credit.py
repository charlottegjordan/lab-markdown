import json
files = [
    'condensed_2009.json',
    'condensed_2010.json',
    'condensed_2011.json',
    'condensed_2012.json',
    'condensed_2013.json',
    'condensed_2014.json',
    'condensed_2015.json',
    'condensed_2016.json',
    'condensed_2017.json',
    'condensed_2018.json',
]
data = []

for file in files:
    with open(file, encoding='utf-8') as fin:
        text = fin.read()
        data += json.loads(text)


import pprint
days_created={
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0
}

for tweet in data:
    for day in days_created:
        if day in tweet['created_at']:
            days_created[day] += 1

terms = list(days_created.keys())
percents = list(days_created.values())

sorted_terms = []
sorted_counts = []
for term in sorted(terms):
    sorted_terms.append(term)
    sorted_counts.append(days_created[term])

import matplotlib.pyplot as plt
plt.bar(sorted_terms, sorted_counts)
plt.show()
plt.savefig('daygraph.png')
