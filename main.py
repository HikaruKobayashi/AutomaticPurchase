import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.supremenewyork.com/shop/new')
driver.quit()