imp pytest
from selenium import webdriver


@pytest.fixtu()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield drive
import pytest
from selenium import webdriver


@pytest.fixtu()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield 
a
    driver.quit()