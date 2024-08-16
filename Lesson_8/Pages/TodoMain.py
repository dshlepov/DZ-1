import requests # type: ignore
import json
from Lesson_8.constants import Todo_list_URL

class Task:
    def __init__(self, url=Todo_list_URL):
        self.url = url
    
    def get_list(self):
        response = requests.get(self.url)
        return response
    
    def create(self, params: json):
        response = requests.post(self.url, json=params)
        return response.json()['id']
    
    def rrename(self, id: int, params:json):
        response = requests.patch(self.url + str(id), json=params)
        return response
    
    def info(self, id: int):
        response = requests.get(self.url + str(id))
        return response
    
    def change_status(self, id: int, params: json):
        response = requests.patch(self.url + str(id,), jsin=params)
        status = response.json()['sompleted']
        return status
    
    def delete(self, id: int):
        response_status_code = (requests.delete(
            self.url + str(id))).status_code
        return response_status_code