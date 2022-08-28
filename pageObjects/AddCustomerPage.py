import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    lnk_Customers_menu_xpath = "//a[@href='#']//*[contains(text(),'Customers')]/i"
    lnk_Customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//*[contains(text(),'Customers')]"
    btn_Addnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_Email_id = "Email"
    txt_Password_id = "Password"
    txt_FirstName_id = "FirstName"
    txt_LastName_id = "LastName"
    rd_Male_id = "Gender_Male"
    rd_Female_id = "Gender_Female"
    txt_DOB_id = "DateOfBirth"
    txt_Companyname_id = "Company"
    txt_Customerroles_xpath = "//label[@for='SelectedCustomerRoleIds']//parent::*//parent::*//parent::*//following-sibling::*//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_Administrators_xpath = "//select[@id='SelectedCustomerRoleIds']//*[contains(text(),'Administrators')]"
    listitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    listitem_Registered_xpath = "//li[contains(text(),'Registered')]"
    listitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_SelectedCustomerRole_id = "SelectedCustomerRoleIds"
    drp_mgrVendor_id = "VendorId"
    txt_AdminComment_id = "AdminComment"
    btn_Save_xpath= "//button[@name='save']"
    wait_icon_xpath = "//a[@class='nav-link'][@data-toggle='dropdown']/i"


    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 30)


    def clickOnCustomersMenu(self):

        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.wait_icon_xpath)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.wait_icon_xpath)))

        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.lnk_Customers_menu_xpath)))
        time.sleep(3)

        self.driver.find_element(By.XPATH,self.lnk_Customers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lnk_Customers_menuitem_xpath)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_Customers_menuitem_xpath)))

        self.driver.find_element(By.XPATH,self.lnk_Customers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_Addnew_xpath)))
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.btn_Addnew_xpath).click()

    def SetEmail(self,email):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.wait_icon_xpath)))
        self.driver.find_element(By.ID,self.txt_Email_id).send_keys(email)

    def SetPassword(self,Password):
        self.driver.find_element(By.ID,self.txt_Password_id).send_keys(Password)

    def SetFirstName(self,fnmae):
        self.driver.find_element(By.ID,self.txt_FirstName_id).send_keys(fnmae)

    def SetLastName(self,lnmae):
        self.driver.find_element(By.ID,self.txt_LastName_id).send_keys(lnmae)

    def SetDOB(self,dob):
        self.driver.find_element(By.ID,self.txt_DOB_id).send_keys(dob)

    def SetCompanyName(self,comnmae):
        self.driver.find_element(By.ID,self.txt_Companyname_id).send_keys(comnmae)

    def SetCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txt_Customerroles_xpath).click()
        time.sleep(3)

        if role == "Registered":
            self.listitem= self.driver.find_element(By.XPATH,self.listitem_Registered_xpath)

        elif role == "Administrators":
            self.listitem= self.driver.find_element(By.XPATH,self.listitem_Administrators_xpath)

        elif role == "Guests":
            # Here user can be Registered (or) Guests only one

            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']//span[@title='delete']").click()
            time.sleep(3)


            self.listitem= self.driver.find_element(By.XPATH,self.listitem_Guests_xpath)

        elif role == "Vendors":
            self.listitem= self.driver.find_element(By.XPATH,self.listitem_Vendors_xpath)

        else:
            self.listitem= self.driver.find_element(By.XPATH,self.listitem_Guests_xpath)

        time.sleep(3)
        print(self.listitem)

        self.driver.execute_script("arguments[0].click();",self.listitem)
        #self.driver.find_element(self.txt_Customerroles_xpath).click()


    def SetManagerofvendor(self,value):
        drp = Select(self.driver.find_element(By.ID,self.drp_mgrVendor_id))
        drp.select_by_visible_text(value)

    def SetGender(self,gender):

        if gender=="Male":
            self.driver.find_element(By.ID,self.rd_Male_id).click()

        if gender=="Female":
            self.driver.find_element(By.ID,self.rd_Female_id).click()

        else:
            self.driver.find_element(By.ID,self.rd_Male_id).click()


    def SetAdminComment(self,comment):
        self.driver.find_element(By.ID,self.txt_AdminComment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btn_Save_xpath).click()





