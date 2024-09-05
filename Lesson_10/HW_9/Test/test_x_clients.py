import pytest
import allure
from Lesson_9.Pages.Employee import Employer
from Lesson_9.Pages.DataBase import DataBase
from Lesson_9.conftest import url

api = Employer(url)
db = DataBase("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.epic("x-clients")
@allure.severity(severity_level='normal')
@allure.title("Сапсок сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Evgen testers', 'cool_company')
    with allure.step("БД - получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
    with allure.step("БД - получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.gett_list_employer(max_id)
    with allure.step("API - получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем списки сотрудников полученных из БД и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("БД - удаляем созданного сотрудника"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("БД - удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудника")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию")
@allure.feature('Тест 2')
def test_add_new_employer():
    db.create_company('Evgen adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    with allure.step("Сравниваем ID компании"):
        assert response['companyId'] == max_id
    with allure.step("Сравниваем имя сотрудника с заданым"):
        assert response["firstName"] == "Dmitry"
    with allure.step("Удостоверяемся что статус сотрудника - True"):
        assert response["isActive"] == True
    with allure.step("Сравниваем фамилию сотрудника с заданной"):
        assert response["lastName"] == "Shikov"
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Сравнение информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника")
@allure.feature('Тест 3')
def test_assertion_data():
    db.create_company('Employer get id compaany', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
    employer_id = db.get_employer_id(max_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Dmitry"
        assert get_api_info["lastName"] == "Shikov"
        assert get_api_info["phone"] == "89998765432"
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Изменение информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотрудника")
@allure.feature('Тест 4')
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Victor", "Shikov", "89998765432")
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Dmitry", employer_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Dmitry"
        assert get_api_info["lastName"] == "Shikov"
        assert get_api_info["isActive"] == True
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - удаляем последнюю созданную компанию"):
        db.delete(max_id)