"""https://admin-demo.nopcommerce.com/admin/"""
import logging

import pytest
from selenium  import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_ddt_login(self,setup):

        self.logger.info("***************** Test_002_DDT_Login *****************")
        self.logger.info("***************** Verify DDT Login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp= LoginPage(self.driver)

        self.row = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Row :",self.row)

        lst_status= [] # Empty list
        for r in range(2,self.row+1):
            self.user= XLUtils.readData(self.path,'Sheet1',r,1)
            self.password= XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp= XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassord(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title and self.exp=="pass" :
                self.logger.info("********** Pass *********")
                time.sleep(10)
                self.lp.clickLogout()
                lst_status.append("Pass")

            elif act_title == exp_title and self.exp=="fail" :
                self.logger.info("********** Fail *********")
                self.lp.clickLogout()
                lst_status.append("Fail")

            elif act_title != exp_title and self.exp=="pass" :
                self.logger.info("********** Fail *********")
                lst_status.append("Fail")


            elif act_title != exp_title and self.exp=="fail" :
                self.logger.info("********** Pass *********")
                lst_status.append("Pass")


        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test Passed ***")
            self.driver.close()
            assert True

        else:
            self.logger.info("**** Login DDT test Failed ***")
            self.driver.close()
            assert False


        self.logger.info("**** End of Login DDT test ***")
        self.logger.info("**** Completed Test_002_DDT_Login ***")



