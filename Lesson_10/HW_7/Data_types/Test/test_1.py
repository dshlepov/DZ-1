import pytest
from Lesson_7.Data_types.Pages.MainPage import MainPage
import allure

values_dict = {'first-name': 'Иван', 'last-name': 'Петров', 'address': 'Ленина, 55-3',
                'e-mail': 'test@skypro.com', 'city': 'Москва', 'country': 'Россия',
                'job-position': 'QA', 'phone': '+7985899998787', 'company': 'CkyPro', 'zip-code': ''}

alert_danger_color = "rgba(248, 215, 218, 1)"
alert_success_color = "rgba(209, 231, 221, 1)"

fields_to_test_success = [
    key for key in values_dict.keys() if key != 'zip-code']

@allure.epic("Data types - registration from")
@allure.severity(severity_level='normal')
@allure.title("Заполнение формы")
@allure.description("Заполнение формы различными данными и проверка валидации данных")
@allure.feature('Тест 1')

@allure.step("Переходим по ссылке в сервис, заполняем поля")
@pytest.fixture(scope="function")
def setup_from(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.open()
    main_page.fill_fields(values_dict)
    main_page.click_submit()
    return main_page

@allure.step("Сравниваем цвет поля почтового индекса")
def test_alert_color(setup_from):
    color_zip = setup_from.find_element_property("zip-code")
    assert color_zip == alert_danger_color

@allure.step("Сравниваем цвет остальных полей")
@pytest.mark.parametrize('selector', fields_to_test_success)
def test_succcess_color(setup_from, selector):
    color = setup_from.find_element_property(selector)
    assert color == alert_success_color