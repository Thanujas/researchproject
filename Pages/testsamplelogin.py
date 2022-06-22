from selenium.webdriver.common.by import By
from Pages.Homepage import HomePage
from Utils.loginlocators import SignInPageLocators
import time
from Utils.testdata import Test_Data


class testpage(HomePage):


    def __init__(self,driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(testpage, self).__init__(driver)

    def set_password(self, password):
        time.sleep(3)
        self.find_element(self.locator.password).send_keys(password)



    def do_login(self):
        n= len(self.locator.akax)
        i=0
        while i < n:
            x = (self.locator.akax[i])
            m=(By.XPATH,x)
            self.do_send_keys(m,Test_Data.bankcode)
            i += 1
            time.sleep(2.4)



    def do_maximumlength(self):

       self.do_send_keys(self.locator.bankcode,Test_Data.randomstring)
       self.do_send_keys(self.locator.username,Test_Data.randomnumbers)
       self.do_send_keys(self.locator.password,Test_Data.randomcombination)
       self.do_click(self.locator.sign)

