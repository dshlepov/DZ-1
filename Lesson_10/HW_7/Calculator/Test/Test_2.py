from Lesson_7.Calculator.Pages.Calcpage import Calcpage
import allure

@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результата вычисления")
@allure.feature('Тест 2')
def test_calculator(chrome_browser):
    delay = 45
    result = 15
    keys_press = '7+8='
    with allure.step("Открываем калькулятор, вводим значения и ожидаем результат"):
        calc = Calcpage(chrome_browser)
        calc.open()
        calc.set_delay(delay)
        calc.input_text(keys_press)
        calc.wait_result(delay, result)

    with allure.step("Сравниваем получившийся результат с ожидаемым"):
        assert calc.result_text() == str(result)