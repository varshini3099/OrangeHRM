import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test_001_Login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()

    def test_homePageLogin(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        result_title = self.driver.title
        if result_title == "OrangeHRM":
            print(f"{result_title} Success")
            assert True
            self.logger.info("Home Page Launching is Success")
        else:
            self.logger.info("Home Page Launching is Failed")
            assert False
        self.driver.close()

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(10)
        self.login_page = Login(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        result_title = self.driver.title
        if result_title == "OrangeHRM":
            print(f"{result_title} Success")
            assert True
            self.logger.info("Login is Success")
        else:
            self.logger.info("Login is Failed")
            assert False
        self.driver.close()
