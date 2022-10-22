from src.bmi import *
from src.msje import *
from src.user import *
import pytest


@pytest.fixture
def user():
    return User()


def test_inches_to_cm():
    assert MSJE.inches_to_cm(75) == 190.5


def test_msje_yintercept_male():
    assert MSJE.yintercept('male') == 5


def test_msje_yintercept_female():
    assert MSJE.yintercept('female') == -161


def test_bmr():
    assert MSJE.bmr(276.2, 75, 54, 'male') == 2178
    assert MSJE.bmr(268.8, 75, 54, 'male') == 2145
    assert MSJE.bmr(174, 75, 54, 'male') == 1715


def test_target_kcals(user):
    user.read_user_from_json_file('tests/test_user.json')
    target_weight_lbs = BMI.height_inches_bmi_to_weight_lbs(
        user.dict_of_user['height_inches'], 21.7)
    assert target_weight_lbs == 174
    assert MSJE.target_kcal_user_target_weight_lbs(
        user, target_weight_lbs) == 1660
