from src.randomfoods import RandomFoods
from src.foods import Foods

import pytest
import random


@pytest.fixture
def foods():
    return Foods()


@pytest.fixture
def randomfoods():
    return RandomFoods()


def test_constructor(randomfoods):
    assert isinstance(randomfoods, RandomFoods)
    assert randomfoods.dict_of_random_foods == {}


def test_foods_to_randomfoods(foods, randomfoods):
    foods.read_foods_from_json_file('tests/test_randomfoods.json')
    assert foods.len() == 19
    randomfoods.foods_to_randomfoods(
        foods, 10, set_random_seed=1)
    assert randomfoods.len() >= 10
    assert sorted(randomfoods.dict_of_random_foods.keys()) == \
        sorted(['chobani yogurt with honey', 'cheerios and almondmilk', 'ribeye steak', 'chobani yogurt',
                'potato with vbutter', 'split pea soup', 'toast with earth balance', 'toast with chao',
                'salad with vranch dressing', 'honeycrisp apple'])


def test_foods_to_randomfoods_two(foods, randomfoods):
    foods.read_foods_from_json_file('tests/test_randomfoods.json')
    assert foods.len() == 19
    randomfoods.foods_to_randomfoods(
        foods, 15, set_random_seed=2)
    assert randomfoods.len() == 15
    print(randomfoods.dict_of_random_foods.keys())
    assert sorted(randomfoods.dict_of_random_foods.keys()) == \
        sorted(['black beans and onions', 'cheerios and almondmilk', 'tofurky chao mayo sandwich',
                'special k and almond milk', 'toast with chao', 'toast with just egg', 'toast with hummus',
                'salad with vranch dressing', 'chobani yogurt with honey', 'split pea soup', 'chobani yogurt',
                'almondmilk', 'salad with anlvr dressing', 'green beans', 'yellow peach'])
