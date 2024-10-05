"""
 Name : Harish Kumar
 Date : 05-Oct-2024
 Program 1 : Using python selenium try to fetch.
            1. Title of the webpage
            2. Current URL of the webpage
            3. Extract entire contents of the webpage and save it whose name will be "web_page_task_11.txt".
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoAutomation:
    def __init__(self, driver_path, url, username, password):
        # Initialize the Chrome WebDriver
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)  
        self.url = url
        self.username = username
        self.password = password

    def open_page(self):
        self.driver.get(self.url)
         
         # login field
    def login(self):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.clear()
        username_field.send_keys(self.username)

        # password field
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.clear()
        password_field.send_keys(self.password)

        # Wait for the login button
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()

    def get_page_info(self):
        # title of the webpage
        title = self.driver.title
        print(f"Title of the webpage: {title}")

        # current URL of the webpage
        current_url = self.driver.current_url
        print(f"Current URL of the webpage: {current_url}")

        page_content = self.driver.page_source
        with open("web_page_task_11.txt", "w", encoding="utf-8") as file:
            file.write(page_content)

        print("Webpage content saved to 'web_page_task_11.txt'")

    def close_browser(self):
        self.driver.quit()

# Main function
if __name__ == "__main__":
    driver_path = '/path/to/chromedriver' 
    url = 'https://www.saucedemo.com/'
    
    # Initialize credentials
    username = 'standard_user'
    password = 'secret_sauce'
    
    automation = SauceDemoAutomation(driver_path, url, username, password)
    
    automation.open_page()
    automation.login()

    automation.get_page_info()

    # Close the browser
    automation.close_browser()
