import time

import allure
import pytest_html
import pytest
from selenium import webdriver
from Pages.testsamplelogin import testpage
from Pages import testsamplelogin
from TestsF.BaseTest import BaseTest
@allure.story("Smart Test automation framework")
@allure.feature("Login scenarios")
@allure.testcase("Login Test case")
class Test_Loginextra(BaseTest):

 def test_login_page(self):
   with allure.step("Login success"):
    loginPage = testsamplelogin.testpage(self.driver)
    loginPage.do_login()
    time.sleep(5)

 def test_maximum_page(self):
    with allure.step("Maximum"):
     loginPage = testsamplelogin.testpage(self.driver)
     loginPage.do_maximumlength()
     time.sleep(5)

    def tearDown(self):
        self.driver.quit()


