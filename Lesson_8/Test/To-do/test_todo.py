import pytest
from Lesson_8.Pages.TodoMain import Task

zadacha = Task()

def test_todo():
    """Получение списка задач"""
    list = zadacha.get_list()
    """Проверяем, что код ответа 200"""
    assert list.status_code == 200

    """Создание новой задачи"""
    params = {"title": "Автоматизация", "completed": 'false'}
    task = zadacha.create(params)

    """Проверяем, что при создании задачи вернется не пустой ID"""
    assert task is not None

    """Переименование задачи"""
    params = {"title": "Автоматизация - крутая штука"}
    renamed_task = zadacha.rename(task, params)
    """Проверяем, что новое название задачи соответствует заданному"""
    assert renamed_task.json()['title'] == "Автоматизация - крутая штука"

    """Получение информации по созданной задаче"""
    info = zadacha.info(task)
    """Проверяем, что новое название задачи соответствует заданному"""
    assert info.json()['title'] == "Автоматизация - крутая штука"
    """Проверяем, что ID задачи соответствует ID задачи созданной впервые"""
    assert info.json()['id'] == task

    """Отметка задачи - выполнена"""
    params = {"completed": 'true'}
    status_true = zadacha.change_status(task, params)
    """Проверяем, что статус задачи - true"""
    assert status_true == True

    """Снятие отметки задачи - выполнена"""
    params = {"completed": 'false'}
    status_false = zadacha.change_status(task, params)
    """Проверяем, что статус задаччи - false"""
    assert status_false == False

    """Удаление задачи"""
    deleting = zadacha.delete(task)
    """Проверякм, что код лтвета 204"""
    assert deleting == 204