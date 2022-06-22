from selenium.webdriver.common.by import By
from Pages.Homepage import HomePage
from Utils.loginlocators import SignInPageLocators, prr
import time
from Utils.testdata import Test_Data
class test(HomePage):


    def __init__(self,driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(test, self).__init__(driver)

    def set_password(self, password):
        time.sleep(3)
        self.find_element(self.locator.password).send_keys(password)



    def do_login(self):
         for i in range(0, self.locatorarraylength1):
          n = (prr[i])
         self.do_send_keys(By.XPATH,self.locator.n,Test_Data.bankcode)
         

    def do_maximumlength(self):

       self.do_send_keys(self.locator.bankcode,Test_Data.randomstring)
       self.do_send_keys(self.locator.username,Test_Data.randomnumbers)
       self.do_send_keys(self.locator.password,Test_Data.randomcombination)
       self.do_click(self.locator.sign)


