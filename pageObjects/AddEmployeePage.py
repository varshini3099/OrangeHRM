import time

from selenium.webdriver.common.by import By

class AddEmployee:

    lnkPIM_menu_path = "//aside//nav//ul/li/a/span[text()='PIM']"
    btnAddnew_xpath = "//button[text()=' Add ']"
    txtFirstName_xpath = "//input[@name='firstName']"
    txtMiddleName_xpath = "//input[@name='middleName']"
    txtLastName_xpath = "//input[@name='lastName']"
    txtEmpId = "//input[contains(@class, 'oxd-input--active')]"
    btnSave_xpath = "//form//button[text()=' Save ']"
    table_xpath = "//div[@class='oxd-table-body']"
    txtEmp_xpath = "//div[contains(text(), 'Admin')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnPIMMenu(self):
        self.driver.find_element(By.XPATH, self.lnkPIM_menu_path).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setMiddlename(self, email):
        self.driver.find_element(By.XPATH, self.txtMiddleName_xpath).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def ListEmployees(self):
        self.driver.find_element(By.XPATH, "//nav//a[text()='Employee List']").click()

    def searchEmployee(self, name):
        self.ListEmployees()
        time.sleep(5)
        return self.driver.find_element(By.XPATH, "//div[contains(text(), '{name}')]").text






