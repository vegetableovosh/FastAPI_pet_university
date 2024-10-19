import json
from uuid import uuid4


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


async def test_delete_user(client, create_user_id_database, get_user_from_database):
    user_data = {
        "user_id": uuid4(),
        "name": "Nikolay",
        "surname": "Svirid",
        "email": "lol@kek.com",
        "is_active": True
    }
    await create_user_id_database(**user_data)
    response = client.delete(f"/user/?user_id={user_data['user_id']}")
    assert response.status_code == 200
    assert response.json() == {"deleted_user_id": str(user_data["user_id"])}
    user_from_db = await get_user_from_database(user_data['user_id'])
    user_from_db = dict(user_from_db[0])
    assert user_from_db['name'] == user_data['name']
    assert user_from_db['surname'] == user_data['surname']
    assert user_from_db['email'] == user_data['email']
    assert user_from_db['is_active'] is True
    assert user_from_db['user_id'] == user_data['user_id']


async def test_get_user(client, create_user_id_database, get_user_from_database):
    user_data = {
        "user_id": uuid4(),
        "name": "Nikolay",
        "surname": "Svirid",
        "email": "lol@kek.com",
        "is_active": True
    }
    await create_user_id_database(**user_data)
    response = client.get(f"/user/?user_id={user_data['user_id']}")
    assert response.status_code == 200
    user_from_db = response.json()
    assert user_from_db['user_id'] == str(user_data["user_id"])
    assert user_from_db['name'] == user_data["name"]
    assert user_from_db['surname'] == user_data["surname"]
    assert user_from_db['email'] == user_data["email"]
    assert user_from_db['is_active'] == user_data["is_active"]


async def test_update_user(client, create_user_in_database, get_use_from_database):
    user_data = {
        "user_id": uuid4(),
        "name": "Nikolay",
        "surname": "Svirid",
        "email": "lol@kek.com",
        "is_active": True
    }
    user_data_updated = {
        "name": "Misha",
        "surname": "Ivanov",
        "email": "lreeefol@kek.com",
    }
    await create_user_in_database(**user_data)
    response = client.patch(f"/user/?user_id={user_data['user_id']}", data=json.dumps(user_data_updated))
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['updated_user_id'] == str(user_data['user_id'])
    user_from_db = await get_use_from_database(user_data['user_id'])
    user_from_db = dict(user_from_db[0])
    assert user_from_db['name'] == user_data['name']
    assert user_from_db['surname'] == user_data['surname']
    assert user_from_db['email'] == user_data['email']
    assert user_from_db['is_active'] is user_data["is_active"]
    assert user_from_db['user_id'] == user_data['user_id']





