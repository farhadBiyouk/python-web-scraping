from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/premier-league-table'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
rows = table.findAll('tr')
for row in rows:
	data_table = []
	for head in row.find_all('th'):
		head_data = head.text.replace('\n', '').strip()
		data_table.append(head_data)
	for body in row.find_all('td'):
		body_data = body.text.replace('\n', '').strip()
		data_table.append(body_data)
	print(data_table)
