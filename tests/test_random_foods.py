from src.randomfoods import RandomFoods
from src.foods import Foods
from src.items import Items
from src.recipes import Recipes

import pytest
import random


@pytest.fixture
def items():
    return Items()


@pytest.fixture
def recipes():
    return Recipes()


@pytest.fixture
def foods():
    return Foods()


@pytest.fixture
def randomfoods():
    return RandomFoods()


def test_constructor(randomfoods):
    assert isinstance(randomfoods, RandomFoods)
    assert randomfoods.dict_of_random_foods == {}


def test_foods_to_randomfoods(items, recipes, foods, randomfoods):
    items.add_items_from_json_file('tests/test_items_randomfoods.json')
    recipes.set_recipes_from_json_file('tests/test_recipes_randomfoods.json')
    foods.recipes_to_foods(items, recipes)
    assert foods.len() == 19
    randomfoods.foods_to_randomfoods(
        items, recipes, foods, 10, set_random_seed=1)
    assert randomfoods.len() >= 12
    assert sorted(randomfoods.dict_of_random_foods.keys()) == \
        sorted(['honeycrisp apple', 'toast with hummus', 'toast with just egg', 'chobani yogurt with honey',
                'cheerios and almondmilk', 'ribeye steak', 'chobani yogurt', 'potato with vbutter', 'split pea soup',
                'toast with earth balance', 'toast with chao', 'salad with vranch dressing'])


def test_foods_to_randomfoods(items, recipes, foods, randomfoods):
    items.add_items_from_json_file('tests/test_items_randomfoods.json')
    recipes.set_recipes_from_json_file('tests/test_recipes_randomfoods.json')
    foods.recipes_to_foods(items, recipes)
    assert foods.len() == 19
    randomfoods.foods_to_randomfoods(
        items, recipes, foods, 10, set_random_seed=2)
    assert randomfoods.len() == 11
    assert sorted(randomfoods.dict_of_random_foods.keys()) == \
        sorted(['black beans and onions', 'cheerios and almondmilk', 'chobani yogurt with honey', 'honeycrisp apple',
                'salad with vranch dressing', 'special k and almond milk', 'split pea soup', 'toast with chao',
                'toast with hummus', 'toast with just egg', 'tofurky chao mayo sandwich'])
