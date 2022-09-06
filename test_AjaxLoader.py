import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("/Users/soprano/Desktop/First_Module/pythonSelenium/chromedriver ")
driver = webdriver.Chrome(service=s)


driver.get("http://webdriveruniversity.com/index.html")

def test_Ajax_Loader():
    driver.find_element(By.CSS_SELECTOR, "#ajax-loader").click()
    ajax_loader_window = driver.window_handles[1]
    driver.switch_to.window(ajax_loader_window)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@type='button']")))
    driver.find_element(By.XPATH, "//span[@type='button']").click()

    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h4")))
    assert "Well Done For Waiting....!!!" in driver.find_element(By.TAG_NAME, "h4").text

    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    HomePage_header = driver.find_element(By.CSS_SELECTOR, "#udemy-promo-thumbnail h1").text
    assert "My Courses & Promo Codes" in HomePage_header, "Maybe, You're not at Home Page"
    driver.close()

test_Ajax_Loader()