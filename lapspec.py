#FFFFFFimport requests
import bs4
from bs4 import BeautifulSoup
import csv

res = requests.get('https://pricebaba.com/laptop/dell-vostro-35787-a553109win9-i5-8th-gen-8gb-1tb-win-10-2gb-gfx')
soup = bs4.BeautifulSoup(res.text, '1xml')
cav_file = open('cms_lapspec.csv', 'w')

csv_writer = csv.writer (csv_file)
csv_writer.writerow(['specs'])
results = soup.find('div', attrs={'id':'productPage'})
for x in results:
	data= x.find_all('td')
	for i in data:	
		specs = i.text
		print("\n", specs)

		print ()
		CSV_writer.writerow([specs])

cav_file.close()

#gitchange
