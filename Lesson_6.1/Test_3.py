from selenium.webdriver.common.by import By
from configuration  import *

def test_shop_from(chrom_browser):
    chrom_browser.get(URL_3)
    chrom_browser.find_element(By.ID, "user-name").send_keys("standsrd_user")
    chrom_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrom_browser.find_element(By.ID, "login-button").click()
    chrom_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrom_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrom_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrom_browser.find_element(By.ID, "shopping_cart_container").click()
    chrom_browser.find_element(By.ID, "checkout").click()
    chrom_browser.find_element(By.ID, "first-name").send_keys("Evgen")
    chrom_browser.find_element(By.ID, "last-name").send_keys("Voronov")
    chrom_browser.find_element(By.ID, "postal-code").send_keys("601500")
    chrom_browser.find_element(By.ID, "continue").click()
    total_price = chrom_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total
    print("Итоговая сумма равна $58.29")