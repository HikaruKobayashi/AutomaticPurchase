from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.co.jp')
driver.quit()