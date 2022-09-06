
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/Users/soprano/Desktop/First_Module/pythonSelenium/chromedriver ")
driver = webdriver.Chrome(service=s)

driver.get('https://www.google.com/?hl=ru')
print(driver.title)
print(driver.current_url)

driver.close()