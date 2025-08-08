import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
def test_saucedemo_purchase_flow(driver):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Configure these variables with your credentials
    USERNAME = "sindhu"
    PASSWORD = "1234567890"
    LOGIN_URL = "https://scale.manage.security.cisco.com/"

    # Set up Selenium WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed

    try:
        # Navigate to the login page
        driver.get(LOGIN_URL)

        # Wait for page to load and elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        # Fill in username and password
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(USERNAME)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)

        # Click the login button
        login_button = driver.find_element(By.ID, "login-button")  # Adjust ID if different
        login_button.click()

        # Wait for login to complete (adjust as needed)
        time.sleep(5)

        # Add verification that login was successful
        print("Login process completed")

    finally:
        # Close the browser
        driver.quit()




