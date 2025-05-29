from selenium.webdriver.common.by import By
class Login:
    loginURL = "//*[@type='submit']"
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    logout = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.loginURL).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout).click()

