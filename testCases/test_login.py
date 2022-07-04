"""https://admin-demo.nopcommerce.com/admin/"""
import pytest
from selenium  import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("***************** Verify Home Page Title  *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login" :
            assert True
            self.logger.info("***************** Verify Home page title test is passed *****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("***************** Verify Home page title test is failed *****************")
            assert False
            self.driver.close()


    def test_login(self,setup):

        self.logger.info("***************** Verify Login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassord(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration" :
            assert True
            self.logger.info("***************** Verify Login test is passed *****************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("***************** Verify Login test is failed *****************")
            assert False
            self.driver.close()






