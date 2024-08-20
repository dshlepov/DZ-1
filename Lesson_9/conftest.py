import pytest
import requests # type: ignore
from Lesson_9.conftest import X_client_URL

@pytest.fixture()
def get_token(username='raphael' , password='cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token