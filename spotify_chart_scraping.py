import time
import requests
from bs4 import BeautifulSoup
import csv
import pprint

url = "https://spotifycharts.com/regional/jp/daily/"

with open('date.csv', encoding = "utf-8-sig") as f:
    reader = csv.reader(f)
    l = [row for row in reader][0]
    print(l)

for a in l:
	res = requests.get(url + a)
	soup = BeautifulSoup(res.text, 'html.parser')
	artists = [i.get_text() for i in soup.select(".chart-table-track > span")]
	titles = [i.get_text() for i in soup.select(".chart-table-track > strong")]
	points = [i.get_text() for i in soup.select(".chart-table-streams")]
	points.pop(0)
	nums = [i+1 for i in range(200)]
	
	ans = []
	#ans.append(nums)
	ans.append(titles)
	ans.append(artists)
	ans.append(points)
	print(ans)

	
	with open("datas/" + a + '.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(ans)
	time.sleep(2)
