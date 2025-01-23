import pandas
from bs4 import BeautifulSoup
import requests

title_data = []
status_data = []
teacher_data = []
time_data = []
price_data = []

url = 'https://www.mongard.ir/courses/?page='
for page in range(1, 5):
	
	response = requests.get(url + str(page))
	soup = BeautifulSoup(response.text, 'html.parser')
	result = soup.select('a.d-block')
	for title in result:
		title_data.append(title.text.strip())
	
	result_status = soup.select('div.custom-btn-course-status span')
	for status in result_status:
		status_data.append(status.text.strip())
	
	result_teacher = soup.select('div.card-details > span:nth-of-type(1)')
	for teacher in result_teacher:
		teacher_data.append(teacher.text.strip())
		
	
	result_time = soup.select('div.card-footer span:nth-of-type(1)')
	for time in result_time:
		time_data.append(time.text.strip())
	
	result_price = soup.select('div.card-footer span:nth-of-type(2)')
	for price in result_price:
		price_data.append(price.text.strip())
	
products = {'Title': title_data, 'Status': status_data, 'Teacher': teacher_data, 'Time': time_data, 'Price': price_data}

data = pandas.DataFrame.from_dict(products, orient='index')

data = data.transpose()
writer = pandas.ExcelWriter('product.xlsx')
data.to_excel(writer)
writer._save()
