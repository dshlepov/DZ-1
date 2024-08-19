from selenium.webdriver.common.by import By
from Lesson_7.constants import URL_3

class Loginpage:
    def __init__(self, browser, url=URL_3):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    
    def sign_in(self, user_name, password):
        self.browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()