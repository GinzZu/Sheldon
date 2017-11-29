import requests
import config
from time import sleep


def check_last_update_id(request):                      # получает последнее обновление на сервере и его Id
    results = request['result']
    total_updates = len(results) - 1
    last_update = results[total_updates]
    return last_update


def send_request_to_log():                              # Отправляет запрос на сервер
    answer = requests.get(config.url + 'getUpdates')
    return answer.json()


def get_id(info):                                       # Получает id чата , из которого пришло обновление
    chat_id = info['message']['chat']['id']
    return chat_id


def get_updates(param, request, timeout):               # Получает обновление со смещением относительно самого первого
    params = {'offset': param, 'timeout': timeout}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def start_examine_content():                            # Проверяет лог обновлений ждет пока появится хотя бы одно для
                                                        # корректного запуска
    buffer_list = []
    while len(buffer_list) == 0:
        buffer_list = send_request_to_log()['result']
        sleep(config.sleep_time)
    return send_request_to_log()


def type_of_update(mess_from_user, mess):               # Определяет тип обновления и отвечает в зависимотси от него
    if mess_from_user[5] == 'entities' and mess['message']['chat']['id'] > 0 and mess['message']['from']['is_bot'] == False and mess['message']['text'] == "/start" :
        person_id = mess['message']['from']['id']
        send_mess_toperson(person_id)
   # elif mess_from_user[4] == 'text' and mess['message']['text'] == "/setbirthday"
        #type_id = person_id
    elif mess_from_user[4] == 'new_chat_participant' and mess['message']['new_chat_participant']['id'] == 467092924:
        chat_id = mess['message']['chat']['id']
        send_mess_togroup(chat_id)
        #type_id = chat_id
    else:
        pass
    #return type_id


def send_mess_toperson(person_id):
    params = {'chat_id': person_id, 'text': 'чтобы внести себя в базу наипиши свои имя фамилию и дату рождения в формате /setbirthday Иван Иванов дд/мм/гггг, если хочешь поменять данные веди /reset данные'}
    response = requests.post(config.url + 'sendMessage', data=params)
    return response



# def search_database(person_id, data_base):
#
#     for item in data_base:
#         if person_id == item:
#             return 1
#         elif person_id != item:
#             return 0
#

def send_mess_togroup(chat_id):                             # Отправляет сообщение в групповой чат
    params = {'chat_id': chat_id, 'text': 'Хей, я бот ,который будет отвечать за '
                'праздники и напоминать о них , если ты ,сволочь ,о них забудешь . '
                                          'Добавь меня в личку. with Love @HOOliganJimmybot P.S. Придумайте название своей тимы, чтобы я знал кто в какой команде, а чтобы его утвердить напишите /setname Название , а если хотите поменять /rename название))'}
    response = requests.post(config.url + 'sendMessage', data=params)
    return response


def main():
    up_id = check_last_update_id(start_examine_content())['update_id']
    data_base = []
    while True:
        mess_from_user = get_updates(up_id, config.url, timeout=4)['result']
        if len(mess_from_user) == 0:
            pass
        else:
            mess = mess_from_user[0]
            print(mess_from_user[0])
            mess_from_user = list(mess_from_user[0]['message'])
            type_of_update(mess_from_user, mess)
            print(mess_from_user)
            up_id += 1
        sleep(config.sleep_time)


if __name__ == '__main__':
    main()
