import random
import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddEmployeePage import AddEmployee

class Test_003_Login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()

    def test_AddEmployee(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(10)
        self.login_page = Login(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        time.sleep(5)

        self.addemployee = AddEmployee(self.driver)
        self.addemployee.clickOnPIMMenu()
        time.sleep(10)
        self.addemployee.clickOnAddNew()
        time.sleep(10)
        first_name = "Varshini"
        middle_name = "dfdg"
        self.addemployee.setFirstName(first_name)
        self.addemployee.setMiddlename(middle_name)
        self.addemployee.setLastName("S")
        self.addemployee.clickOnSave()
        self.logger.info(f"Employee {first_name} is added successfully")
        #result_emp = self.addemployee.searchEmployee(first_name)
        #assert result_emp == first_name + middle_name
        # searching for employee
        self.addemployee.clickLogout()
        self.driver.close()

