from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "HbrButton-button")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
