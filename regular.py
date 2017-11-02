import re


def regular():
    zapros = 'Соколов Дмитрий муж 11.03.1997'
    data = re.compile(r'\d+')
    name = re.compile(r'[а-яА-Я]+')
    result1 = data.findall(zapros)
    result2 = name.findall(zapros)
    print(result1, result2,)
regular()


