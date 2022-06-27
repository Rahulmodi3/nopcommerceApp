import string

import pytest
import time
from selenium  import webdriver
import random
import string
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SerachCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SerachCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_serachcustomeName(self,setup):

        self.logger.info("***************** Test_005_SerachCustomerByName *****************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassord(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login Scuessful *****************")

        self.logger.info("***************** Start Serach Customer by Name test *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        searchcus = SerachCustomer(self.driver)
        searchcus.setFirstName("Brenda")
        searchcus.clickSearch()
        time.sleep(5)

        self.logger.info("***************** Seraching Customer by Name *****************")

        status = searchcus.searchCustomerByName("Brenda Lindgren")

        if status==True:
            assert True
            self.logger.info("***************** Seraching Customer Test is Passed *****************")

        else:
            assert False
            self.logger.error("***************** Seraching Customer by Name Test is Fail  *****************")

        self.driver.close()
        self.logger.info("***************** Ending Test_005_SerachCustomerByName Test *****************")


