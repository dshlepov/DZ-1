from selenium.webdriver.common.by import By
from Lesson_7.constants import URL_1

class MainPage:
    def __init__(self, browser, url=URL_1):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.yrl)

    def fill_fields(self, v_dict: dict):
        for key, value in v_dict.items():
            selector = f'[name={key}]'
            self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    def click_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def find_element_property(self, locator):
        background_color = self.browser.find_element(By.ID, locator).value_of_css_property("background-color")
        return background_color