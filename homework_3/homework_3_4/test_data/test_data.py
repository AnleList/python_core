# Создайте собственный модуль test_data.py. В нём реализуйте функции
# generate_login(), generate_age(), generate_status() и
# generate_user().
# generate_user() должна использовать остальные функции и возвращать
# готового тестового пользователя в виде словаря.

import random

def generate_login():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    login = ""
    name_len = 8
    for letter in range(name_len):
        login += random.choice(letters)
    return login

def generate_age():
    return random.randint(18, 80)

def generate_status():
    statuses = ['ACTIVE', 'BLOCKED', 'INACTIVE']
    return random.choice(statuses)

def generate_user():
    return {
        'login': generate_login(),
        'age': generate_age(),
        'status': generate_status()
    }
