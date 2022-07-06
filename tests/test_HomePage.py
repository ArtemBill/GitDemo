import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getExampleCheck().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()

        message = homepage.getMessage().text

        assert "success" in message

    # @pytest.fixture(params=[("Artem", "Bilyk", "Male"), ("Yurii", "Bilyk", "Male")])
    # @pytest.fixture(params=[{"firstname": "Artem", "lastname": "Bilyk", "gender": "Male"}, {"firstname": "Elena", "lastname":
    #     "Bilyk", "gender": "Male"}])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


