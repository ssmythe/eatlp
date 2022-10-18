from src.bmi import *
from src.msje import *
import pytest


def test_inches_to_cm():
    assert MSJE.inches_to_cm(75) == 190.5
    
def test_msje_yintercept_male():
    assert MSJE.yintercept('male') == 5


def test_msje_yintercept_female():
    assert MSJE.yintercept('female') == -161


def test_bmr():
    assert MSJE.bmr(276.2, 75, 54, 'male') == 2178
    assert MSJE.bmr(268.8, 75, 54, 'male') == 2145


def test_t2kcals():
    assert MSJE.t2kcals(276.2, 75, 54, 'male', 'sedentary', 2) == 1614
    assert MSJE.t2kcals(268.8, 75, 54, 'male', 'sedentary', 2) == 1574
    # assert MSJE.t2kcals(268.8, 75, 54, 'male', 'sedentary', 2) == 1558
    # assert MSJE.t2kcals(268.8, 75, 54, 'male', 'light activity', 2) == 1932
