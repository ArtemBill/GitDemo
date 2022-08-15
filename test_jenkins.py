from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)

# s = Service("/Users/soprano/Desktop/First_Module/pythonSelenium/chromedriver ")
# driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(by=By.CSS_SELECTOR, value=".btn-success").click()
assert "Success" in driver.find_element(By.CSS_SELECTOR, value=".alert-success").text
