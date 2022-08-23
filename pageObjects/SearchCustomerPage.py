import time
from selenium.webdriver.common.by import By
class SerachCustomer:
    txt_Email_id = "SearchEmail"
    txt_Firstname_id = "SearchFirstName"
    txt_Lastname_id = "SearchLastName"
    btn_Search_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    tableRow_xpath = "//table[@id='customers-grid']//tbody//tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody//tr/td"


    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_Email_id).clear()
        self.driver.find_element(By.ID,self.txt_Email_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_Firstname_id).clear()
        self.driver.find_element(By.ID,self.txt_Firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txt_Lastname_id).clear()
        self.driver.find_element(By.ID,self.txt_Lastname_id).send_keys(lname)


    def clickSearch(self):
        self.driver.find_element(By.ID,self.btn_Search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRow_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumn_xpath))

    def searchCustomerByEmail(self,email):
        flag= False

        for r in range(1,self.getNoOfRows()+1):
            #table = self.driver.find_element(self.table_xpath)
            eamilid = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
            if eamilid==email:
                flag = True
                break

        return flag

    def searchCustomerByName(self,Name):
        flag= False

        for r in range(1,self.getNoOfRows()+1):
            #table = self.driver.find_element(self.table_xpath)
            name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[3]").text
            if name==Name:
                flag = True
                break

        return flag







