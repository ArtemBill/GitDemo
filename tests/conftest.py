import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )


@pytest.fixture
def setup(request):
    # browser_name = request.config.getoption("browser_name")
    # if browser_name == "chrome":
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

    #
    #     driver.maximize_window()
    # elif browser_name == "firefox":
    #     print("firefox invocation Gecko driver")
    # elif browser_name == "IE":
    #     print("IE invocation")

    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
