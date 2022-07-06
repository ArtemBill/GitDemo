from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    exampleCheck = (By.ID, "exampleCheck1")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CLASS_NAME, "alert-success")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getExampleCheck(self):
        return self.driver.find_element(*HomePage.exampleCheck)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)


