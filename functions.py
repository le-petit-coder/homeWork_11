import json


def load_candidates():
    """Загружает личные данные студентов из файла в список python"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_by_pk(pk):
    """Функция возвращает имя кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["id"]:
                return item


def get_by_skill(skill_name):
    """Функция возвращает кандидатов по наличию навыков"""
    all_candidates = []
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if skill_name in item['skills'].lower().split(', '):
                all_candidates.append(item)
    return all_candidates


def get_by_name(name):
    """Функция возвращает кандидатов по имени"""
    all_names = []
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if name == item["name"]:
                all_names.append(item)
    return all_names


def get_position(pk):
    """Функция возвращает позицию кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["pk"]:
                return item["position"]


def get_skills(pk):
    """Функция возвращает skills кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["pk"]:
                return item["skills"]


def show_candidates(data):
    for i in data:
        return f'<pre>\n \
            Имя кандидата - {i["name"]}\n \
            Позиция кандидата: {i["position"]}\n \
            Навыки через запятую: {i["skills"]}\n \
            \n \
            </pre>'
