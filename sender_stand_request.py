import requests
import configuration


# Функция создает новый заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


# Функция получает заказ по его трек-номеру
def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_TRACK_PATH, params={
        't': track
    })
