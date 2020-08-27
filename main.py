import requests
import schedule
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url='https://www.supremenewyork.com/shop/all'
driver.get(url)
driver.find_element_by_class_name('inner-article').click()
nextUrl = driver.current_url
print (nextUrl)
driver.get(nextUrl)
driver.find_element_by_class_name('continue').click()
driver.quit()