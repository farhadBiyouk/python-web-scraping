from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.get('https://www.varzesh3.com/album')

end_of_scroll = driver.execute_script('return document.body.scrollHeight;')
while True:
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	time.sleep(3)
	now_scroll = driver.execute_script('return document.body.scrollHeight;')
	if now_scroll == end_of_scroll:
		break
	end_of_scroll = now_scroll

images = driver.find_element(By.CSS_SELECTOR,'div.album-cover-image img')

for img in images:
	print(img.get_attribute('src'))