import sys, unittest, time, datetime
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from globalvars import VIDLISTPATH, CHANNELVIDSURL

# credit to banhao
# https://github.com/banhao/scrape-youtube-channel-videos-url/blob/master/scrape-youtube-channel-videos-url.py
# README available there as well
# This assumes you have firefox scraping with Selenium set up
def grab_all_vids():
	driver = webdriver.Firefox()
	#driver = webdriver.Edge()
	# driver = webdriver.Chrome()
	url = CHANNELVIDSURL
	driver.get(url)
	time.sleep(5)
	dt=datetime.datetime.now().strftime("%Y%m%d%H%M")
	height = driver.execute_script("return document.documentElement.scrollHeight")
	lastheight = 0

	# ### If you don't have the Youtube cookie pop-up window issue, you can comment the following codes.
	# consent_button_xpath = "//button[@aria-label='Reject all']"
	# consent = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, consent_button_xpath)))
	# consent = driver.find_element_by_xpath(consent_button_xpath)
	# consent.click()
	# ###

	while True:
		if lastheight == height:
			break
		lastheight = height
		driver.execute_script("window.scrollTo(0, " + str(height) + ");")
		time.sleep(2)
		height = driver.execute_script("return document.documentElement.scrollHeight")

	user_data = driver.find_elements_by_xpath('//*[@id="video-title-link"]')
	for i in user_data:
		link = (i.get_attribute('href'))
		f = open(VIDLISTPATH, 'a+')
		if link:
			f.write(link + '\n')
	f.close()
	driver.quit()
