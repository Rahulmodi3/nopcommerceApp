from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
import time

from selenium  import webdriver


baseURL = "https://admin-demo.nopcommerce.com/admin/"
useremail = "admin@yourstore.com"
password = "admin"


driver=webdriver.Chrome("C:/Users/modir/PycharmProjects/Automation Framework/chromedriver.exe")

driver.get(baseURL)
driver.maximize_window()
lp= LoginPage(driver)
lp.setUsername(useremail)
lp.setPassord(password)
lp.clickLogin()


addcust = AddCustomer(driver)
addcust.clickOnCustomersMenu()
addcust.clickOnCustomersMenuItem()

addcust.clickOnAddnew()

time.sleep(3)

addcust.SetCustomerRoles("Guests")
