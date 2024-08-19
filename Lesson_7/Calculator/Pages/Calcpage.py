from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Lesson_7.constants import URL_2

class Calcpage:
    def  __init__(self, browser):
        self.browser = browser
    
    def open(self):
        self.browser.get(URL_2)
    
    def set_belay(self, delay):
        delay_field = self.browser.find_element(By.CSS_SELECTOR< '#delay')
        delay_field.clear()
        delay_field.send_keys(delay)

    def input_text(self, keys_calculator):
        for val in keys_calculator:
            self.browser.find_element(By.XPATH, f'//span[text()="{val}"]').click()
    
    def wait_result(self, delay, result):
        wainter = WebDriverWait(self.browser, delay +1)
        wainter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'screen'), str(result)))
    
    def result_text(self):
        result = self.browser.find_element(By.CSS_SELECTOR, '.screnn')
        return result.text