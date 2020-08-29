import requests
import schedule
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# url='https://www.supremenewyork.com/shop/all'
# driver.get(url)
# driver.find_element_by_class_name('inner-article').click()
# nextUrl = driver.current_url
nextUrl = 'https://www.supremenewyork.com/shop/accessories/n2dcp4gwu/ulgkp3drz'
driver.get(nextUrl)
size_element = driver.find_element_by_name('size')
size_select_element = Select(size_element)
# 77643 means Large Size by Supreme site
size_select_element.select_by_value('77643')
selector = '#add-remove-buttons > input'
driver.find_element_by_css_selector(selector).click()
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
driver.find_element_by_id('order_billing_name').send_keys("名前", Keys.ENTER)
driver.find_element_by_id('order_email').send_keys("メールアドレス", Keys.ENTER)
driver.find_element_by_id('order_tel').send_keys("電話番号", Keys.ENTER)
prefecture_element = driver.find_element_by_name('order[billing_state]')
prefecture_select_element = Select(prefecture_element)
prefecture_select_element.select_by_value(' 東京都')
payment_element = driver.find_element_by_name('credit_card_type')
payment_select_element = Select(payment_element)
payment_select_element.select_by_value('jcb')