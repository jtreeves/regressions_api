# from app import app, db
# from app.models import User
# from datetime import datetime

# import os
# import tempfile
# import pytest

# from app import app

def test_index(app, client):
    del app
    res = client.get('/')
    print('RES: ', res)
    print('RES.DATA: ', res.data)
    print('RES.DATA[0:10]: ', res.data[0:10])
    assert res.status_code == 200

# def test_create_user():
#     new_user = User(
#         name='Michael',
#         email='michael@email.com',
#         key='ABC123',
#         date=datetime.now()
#     )
#     db.session.add(new_user)
#     db.session.commit()

#     assert new_user.name == 'Michael'
#     assert new_user.email == 'michael@email.com'
#     assert new_user.key == 'ABC123'

# def incrementing(num):
#     return num + 1

# def test_incrementing():
#     assert incrementing(3) == 5

# def decrementing(num):
#     return num - 1

# def test_decrementing():
#     assert decrementing(3) == 1