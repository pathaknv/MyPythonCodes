import os
import sqlite3
from collections import OrderedDict
import operator
import matplotlib.pyplot as plt

data_path = "C:/Users/nikhilvp/AppData/Local/Google/Chrome/User Data/Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')

c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall()

def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print("URL format error!")

sites_count = {} #dict makes iterations easier :D

for url, count in results:
	url = parse(url)
	if url in sites_count:
		sites_count[url] += 1
	else:
		sites_count[url] = 1

sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))
sites_count_sorted = {k: v for k, v in sites_count_sorted.items() if v >= 50}
print(sites_count_sorted)


plt.bar(range(len(sites_count_sorted)), sites_count_sorted.values(), align='edge')
plt.xticks(rotation=45)
plt.xticks(range(len(sites_count_sorted)), sites_count_sorted.keys())
plt.show()
