from src.user import User

import pytest
import sys

@pytest.fixture
def user():
    return User()


def test_constructor(user):
    assert isinstance(user, User)

def test_read_user_from_json_file(user):
    assert user.len() == 0
    user.read_user_from_json_file('tests/test_user.json')
    assert user.len() == 5
    assert user.dict_of_user['current_weight_lbs'] == 266.7
    assert user.dict_of_user['current_age'] == 54
    assert user.dict_of_user['max_kcal'] == 1654
    assert user.dict_of_user['max_sodium'] == 2000
    assert user.dict_of_user['num_of_menus'] == 7
