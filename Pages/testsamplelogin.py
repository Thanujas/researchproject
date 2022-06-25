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
        n= len(self.locator.xpathinalist)
        i=0
        while i < n-1:
         x = (self.locator.xpathinalist[i])
         m=(By.XPATH,x)
         self.do_send_keys(m,Test_Data.Testdatavalues[i])

         i += 1
         time.sleep(2.4)
        else:
         j=(By.XPATH,self.locator.xpathinalist[-1])
        self.do_click(j)



    def do_maximumlength(self):
        n = len(self.locator.xpathinalist)
        i = 0
        while i < n - 1:
            x = (self.locator.xpathinalist[i])
            m = (By.XPATH, x)
            self.do_send_keys(m, Test_Data.randomcombination[i])

            i += 1
            time.sleep(2.4)
        else:
            j = (By.XPATH, self.locator.xpathinalist[-1])
        self.do_click(j)


