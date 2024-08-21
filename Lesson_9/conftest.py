import pytest
import requests # type: ignore
from Lesson_9.conftest import url

@pytest.fixture()
def get_token(username='raphael' , password='cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(url + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
