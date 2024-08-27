import pytest
from Lesson_9.Pages.Employee import Employer
from Lesson_9.Pages.DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_get_list_of_employers():
    db.create_company('Evgen testers', 'cool_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
    db_employer_list = db.gett_list_employer(max_id)
    api_employer_list =  api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete(max_id)

    def test_add_new_employer():
        db.create_company('Evgen adding new employer', 'employer')
        max_id = db.last_company_id()
        db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        assert response['companyId'] == max_id
        assert response["firstName"] == "Dmitry"
        assert response["isActive"] == True
        assert response["lastName"] == "Shikov"
        db.delete_employer(employer_id)
        db.delete(max_id)

    def test_assertion_data():
        db.create_company('Employer get id compaany', 'new')
        max_id = db.last_company_id()
        db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
        employer_id = db.get_employer_id(max_id)
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Dmitry"
        assert get_api_info["lastName"] == "Shikov"
        assert get_api_info["phone"] == "89998765432"
        db.delete_employer(employer_id)
        db.delete(max_id)

        def test_update_user_info():
            db.create_company('New updating company', 'test')
            max_id = db.last_company_id()
            db.create_employer(max_id, "Dmitry", "Shikov", "89998765432")
            employer_id = db.get_employer_id(max_id)
            db.update_employer_info("Victor", employer_id)
            get_api_info = (api.get_info(employer_id)).json()
            assert get_api_info["firstName"] == "Victor"
            assert get_api_info["lastName"] == "Shikov"
            assert get_api_info["isActive"] == True
            db.delete_employer(employer_id)
            db.delete(max_id)
