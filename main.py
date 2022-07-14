from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs

from pprint import pprint as print

from time import sleep



BASE_URL = 'https://www.indeed.com'

driver = webdriver.Firefox()

driver.get('https://indeed.com')

input('Waiting for login, press Enter to run....')

soup = bs(driver.page_source, 'html.parser')

print(f'Found ' + str(len(soup)) + ' jobs')

for a in soup.find_all('a', class_='jcs-JobTitle'):
	driver.get(BASE_URL + a['href'])

	soup = bs(driver.page_source, 'html.parser')

	if soup.find('a', class_='icl-Button'):
		pass

	else:
		apply_bttn = driver.find_element(By.ID, 'indeedApplyButton')
		apply_bttn.click()

		sleep(5)

		cont_bttn = driver.find_element(By.CLASS_NAME, 'ia-continueButton')
		cont_bttn.click()


driver.close()