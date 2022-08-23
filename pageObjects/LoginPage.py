'For Explicit Wait'
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    txt_username_id = "Email"
    txt_password_id = "Password"
    btn_login_xpath = "//button[contains(@class,'login-button')]"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 30)

    def setUsername(self,username):

        self.driver.find_element(By.ID,self.txt_username_id).clear()
        self.driver.find_element(By.ID,self.txt_username_id).send_keys(username)

    def setPassord(self,password):
        self.driver.find_element(By.ID,self.txt_password_id).clear()
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogout(self):

        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.link_logout_linktext)))
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))

        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
