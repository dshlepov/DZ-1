import pytest # type: ignore
from Lesson_9.Pages.Employee import Employer
from Lesson_9.Pages.DataBase import DataBase # type: ignore

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgreaql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

"""Получаем список сотрудников из БД и АПИ, после чего сравниваем их"""
def test_get_list_of_employers():
    db.create_company('Evgen testers', 'cool_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 80020006000)
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete(max_id)

"""Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию"""
def test_add_new_employer():
    db.create_company('Evgen adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    assert response["companyId"] == max_id
    assert response["firctName"] == "Evgen"
    assert response["isActive"] == True
    assert response["lastName"] == "Voronov"
    db.delete_employer(employer_id)
    db.delete(max_id)

"""Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника в БД"""
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id ()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.gey_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Evgen"
    assert get_api_info["lastName"] == "Voronov"
    assert get_api_info["phone"] == "8002000600"
    db.delete_employer(employer_id)
    db.delete(max_id)

"""Сравниваем информацию о сотруднике полученную по ФПИ с измененной информациейв БД информацией о сотруднике"""
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voroniv", 8002000600)
    employer_id =db.get_employer_id(max_id)
    db.update_employer_info("King", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "King"
    assert get_api_info["lastName"] == "Voronov"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)