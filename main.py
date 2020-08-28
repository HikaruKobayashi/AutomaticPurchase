import requests
import schedule
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# url='https://www.supremenewyork.com/shop/all'
# driver.get(url)
# driver.find_element_by_class_name('inner-article').click()
# nextUrl = driver.current_url
nextUrl = 'https://www.supremenewyork.com/shop/accessories/n2dcp4gwu/ulgkp3drz'
# print (nextUrl)
driver.get(nextUrl)
size_element = driver.find_element_by_name('size')
size_select_element = Select(size_element)
# 77643 means Large Size by Supreme site
size_select_element.select_by_value('77643')
selector = '#add-remove-buttons > input'
driver.find_element_by_css_selector(selector).click()
selector = '.sidebar > #cart > .checkout'
driver.find_element_by_css_selector(selector).click()
# driver.quit()