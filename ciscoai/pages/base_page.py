from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_and_find(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_and_find(by_locator).click()

    def type(self, by_locator, text):
        el = self.wait_and_find(by_locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, by_locator):
        return self.wait_and_find(by_locator).text
