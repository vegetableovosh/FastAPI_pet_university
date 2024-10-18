import json

async def test_create_user(client, get_user_from_database):
    user_data = {
        "name": "Nikolay",
        "surname": "Svirid",
        "email": "lol@kek.com"
    }
    response = client.post('/user/', data=json.dumps(user_data))
    data_from_resp = response.json()
    assert response.status_code == 200
    assert data_from_resp['name'] == user_data['name']
    assert data_from_resp['surname'] == user_data['surname']
    assert data_from_resp['email'] == user_data['email']
    user_from_db = await get_user_from_database(data_from_resp['user_id'])
    assert len(user_from_db) == 1
    user_from_db = await get_user_from_database([0])
    assert user_from_db['name'] == user_data['name']
    assert user_from_db['surname'] == user_data['surname']
    assert user_from_db['email'] == user_data['email']
    assert user_from_db['is_active'] is True
    assert str(user_from_db['user_id']) == data_from_resp['user_id']