from Lesson_7.Swag_Labs.Pages.Loginpage import Loginpage
from Lesson_7.Swag_Labs.Pages.Productspage import Productspage
from Lesson_7.Swag_Labs.Pages.Checkoutpage import Checkoutpage

user_name = "standard_user"
password = "secret_sauce"

first_name = "Mark"
last_name = "Markov"
postal_code = "123456"

sum = "$58.29"

def test_purchase(chrome_browser):
    login_page = Loginpage(chrome_browser)
    login_page.open()
    login_page.sign_in(user_name, password)

    products_page = Productspage(chrome_browser)
    products_page.add_to_cart()
    products_page.go_to_cart()
    products_page.checkout_click()

    checkout_page = Checkoutpage(chrome_browser)
    checkout_page.make_checkout(first_name, last_name, postal_code)

    txt = checkout_page.check_total()
    assert sum in txt
