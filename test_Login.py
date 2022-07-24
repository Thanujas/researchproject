import time
import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.LoginPage import LoginPage
from Pages import LoginPage
from TestsF.BaseTest import BaseTest
@allure.story("Smart Test automation framework")
@allure.feature("Basic Smoke Testing")


class Test_Login(BaseTest):
 @allure.testcase("Login  Validation")
 @allure.description("This test case validate whether user can login to the system successfully"
                     )
 @allure.severity(allure.severity_level.CRITICAL)
 @pytest.mark.order(5)
 def test_Verify_successfully_ableto_loginto_System(self):
    with allure.step("Login success"):
     loginPage = LoginPage.LoginPage(self.driver)
     loginPage.do_login()
     allure.attach(self.driver.get_screenshot_as_png(),name="Verify maximum possible charachters",
       attachment_type=AttachmentType.PNG )
     time.sleep(3)

 @allure.testcase("Maximum Charachter Count Validation")

 @allure.description("This test case validate whether user can proceed further by entering maximum possible"
                        "charachter count")
 @allure.severity(allure.severity_level.MINOR)
 @pytest.mark.order(3)
 def test_Verify_System_Maximum_Charachter_Count(self):
    with allure.step("Maximum possible input charachters"):
     loginPage = LoginPage.LoginPage(self.driver)
     loginPage.do_maximumlength()
     allure.attach(self.driver.get_screenshot_as_png(),name="Verify maximum possible charachter count",
       attachment_type=AttachmentType.PNG )
     time.sleep(3)

 @allure.testcase("Minimum Charachter Count Validation")
 @allure.description("This test case validate whether user can proceed further by entering minimum possible"
                     "charachter count")
 @allure.severity(allure.severity_level.NORMAL)
 @pytest.mark.order(4)
 def test_Verify_System_Minimum_Charachter_Count(self):
    with allure.step("Minimum Possible input charachters"):
     loginPage = LoginPage.LoginPage(self.driver)
     loginPage.do_minimumlength()
     allure.attach(self.driver.get_screenshot_as_png(), name="Verify minimum possible charachter count",
                   attachment_type=AttachmentType.PNG)
     time.sleep(3)

 @allure.testcase("Allowable Data Type Validation")

 @allure.description("This test case validate whether user can proceed further by entering all the allowable"
                        "charachter types")
 @allure.severity(allure.severity_level.MINOR)
 @pytest.mark.order(1)
 def test_Verify_Allowable_Charachter_Types(self):
    with allure.step("possible input charachters"):
     loginPage = LoginPage.LoginPage(self.driver)
     loginPage.do_allowable_data_types()
     allure.attach(self.driver.get_screenshot_as_png(), name="Verify allowable charachter types",
                   attachment_type=AttachmentType.PNG)
     time.sleep(3)

 @allure.testcase("NON-Allowable Data Type Validation")

 @allure.description("This test case validate whether user unable to proceed further by entering non allowable"
                        "charachter types")
 @allure.severity(allure.severity_level.MINOR)
 @pytest.mark.order(2)
 def test_Verify_NON_Allowable_Charachter_Types(self):
   with allure.step("possible input charachters"):
    loginPage = LoginPage.LoginPage(self.driver)
    loginPage.do_nonallowable_data_types()
    allure.attach(self.driver.get_screenshot_as_png(), name="Verify non allowable charachter types",
                  attachment_type=AttachmentType.PNG)
    time.sleep(3)

    def tearDown(self):
        self.driver.quit()


