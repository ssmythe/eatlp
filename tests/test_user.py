from src.user import User

import pytest


@pytest.fixture
def user():
    return User()


def test_constructor(user):
    assert isinstance(user, User)


def test_read_user_from_json_file(user):
    assert user.len() == 0
    user.read_user_from_json_file('tests/test_user.json')
    assert user.len() == 11
    assert user.dict_of_user['current_age'] == 54
    assert user.dict_of_user['current_weight_lbs'] == 265.7
    assert user.dict_of_user['height_inches'] == 75
    assert user.dict_of_user['weight_loss_per_week_lbs'] == 2
    assert user.dict_of_user['max_sodium'] == 2000
    assert user.dict_of_user['msje_activity_factor'] == 'sedentary'
    assert user.dict_of_user['max_num_of_menus'] == 7
    assert user.dict_of_user['sex'] == 'male'
    assert user.dict_of_user['start_weight_date'] == '2022-09-14'
    assert user.dict_of_user['start_weight_lbs'] == 276.2
    assert user.dict_of_user['target_bmi'] == 21.7


def test_write_user_to_json_file(user):
    assert user.len() == 0
    user.read_user_from_json_file('tests/test_user.json')
    user.write_user_to_json_file('tests/test_user_2.json')
    user.read_user_from_json_file('tests/test_user_2.json')
    assert user.len() == 11
    assert user.dict_of_user['current_age'] == 54
    assert user.dict_of_user['current_weight_lbs'] == 265.7
    assert user.dict_of_user['height_inches'] == 75
    assert user.dict_of_user['weight_loss_per_week_lbs'] == 2
    assert user.dict_of_user['max_sodium'] == 2000
    assert user.dict_of_user['msje_activity_factor'] == 'sedentary'
    assert user.dict_of_user['max_num_of_menus'] == 7
    assert user.dict_of_user['sex'] == 'male'
    assert user.dict_of_user['start_weight_date'] == '2022-09-14'
    assert user.dict_of_user['start_weight_lbs'] == 276.2
    assert user.dict_of_user['target_bmi'] == 21.7
