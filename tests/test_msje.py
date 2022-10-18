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
    assert MSJE.bmr(174, 75, 54, 'male') == 1715


def test_t2kcals():
    assert MSJE.target_kcals(276.2, 276.2, 174, 75, 54, 'male', 'sedentary', 2) == 1614
    assert MSJE.target_kcals(276.2, 268.8, 174, 75, 54, 'male', 'sedentary', 2) == 1646
    assert MSJE.target_kcals(276.2, 174, 174, 75, 54, 'male', 'sedentary', 2) == 2058

def test_t1kcals():
    assert MSJE.target_kcals(276.2, 276.2, 174, 75, 54, 'male', 'sedentary', 1) == 2114
    assert MSJE.target_kcals(276.2, 268.8, 174, 75, 54, 'male', 'sedentary', 1) == 2110
    assert MSJE.target_kcals(276.2, 174, 174, 75, 54, 'male', 'sedentary', 1) == 2058

def test_t0kcals():
    assert MSJE.target_kcals(276.2, 276.2, 174, 75, 54, 'male', 'sedentary', 0) == 2614
    assert MSJE.target_kcals(276.2, 268.8, 174, 75, 54, 'male', 'sedentary', 0) == 2574
    assert MSJE.target_kcals(276.2, 174, 174, 75, 54, 'male', 'sedentary', 0) == 2058
