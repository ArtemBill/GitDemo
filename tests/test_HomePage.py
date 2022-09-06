# import openpyxl
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

    # def getTestData(self, test_case_name):
    #     book = openpyxl.load_workbook("/Users/soprano/Desktop/PythonSelFramework/TestData/PythonDemo.xlsx")
    #     sheet = book.active
    #     Dict = {}
    #     for i in range(1, sheet.max_row):
    #         for j in range(1, sheet.max_column + 1):
    #             if sheet.cell(row=i, column=j).value == test_case_name:
    #                 Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
    #
    #
    #     print(Dict)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


