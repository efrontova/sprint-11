import sender_stand_request
import data


# Фронтова Елена, 11-я когорта — Финальный проект. Инженер по тестированию плюс

def test_create_order():
    new_order_create_response = sender_stand_request.post_new_order(data.order_body)
    assert new_order_create_response.status_code == 201
    track_number = new_order_create_response.json()['track']

    order_response = sender_stand_request.get_new_order(track_number)
    assert order_response.status_code == 200
