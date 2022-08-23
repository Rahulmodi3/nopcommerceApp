import string

import pytest
import time
from selenium  import webdriver
import random
import string
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):

        self.logger.info("***************** Test_003_AddCustomer *****************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassord(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login Scuessful *****************")

        self.logger.info("***************** Start Add Customer test *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        time.sleep(3)

        self.logger.info("***************** Provide Customer info *****************")

        self.email = random_generator() + "@gmail.com"

        self.addcust.SetEmail(self.email)
        self.addcust.SetPassword("test123")
        self.addcust.SetFirstName("Rahul")
        self.addcust.SetLastName("Kumar")
        self.addcust.SetGender("Male")
        self.addcust.SetDOB("7/27/1998")
        self.addcust.SetCompanyName("busyQA")
        self.addcust.SetCustomerRoles("Guests")
        self.addcust.SetManagerofvendor("Vendor 2")
        self.addcust.SetAdminComment("This for testing ....")
        self.addcust.clickOnSave()

        self.logger.info("***************** Saving Customer info *****************")

        self.logger.info("***************** Add Customer validation is start *****************")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        #print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("***************** Add Customer Test is Passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer.png")
            self.logger.error("***************** Add Customer Test is Fail  *****************")
            assert False

        self.driver.close()
        self.logger.info("***************** Ending Test_003_AddCustomer Test *****************")


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
