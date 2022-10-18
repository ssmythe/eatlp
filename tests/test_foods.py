from src.foods import Foods
from src.items import Items
from src.recipes import Recipes

import pytest


@pytest.fixture
def items():
    return Items()


@pytest.fixture
def recipes():
    return Recipes()


@pytest.fixture
def foods():
    return Foods()


def test_constructor(foods):
    assert isinstance(foods, Foods)
    assert foods.dict_of_foods == {}


def test_recipes_to_foods(items, recipes, foods):
    items.add_items_from_json_file('tests/test_items.json')
    recipes.set_recipes_from_json_file(
        'tests/test_recipes.json')
    foods.recipes_to_foods(items, recipes)
    assert foods.len() == 2

def test_write_foods_to_json_file(foods, items, recipes):
    items.add_items_from_json_file('tests/test_items.json')
    recipes.set_recipes_from_json_file(
        'tests/test_recipes.json')
    foods.recipes_to_foods(items, recipes)
    assert foods.len() == 2
    # write foods
    foods.write_foods_to_json_file('tests/test_foods.json')
    str_json_foods_written = foods.foods_to_json_str()
    # read foods
    foods = Foods()
    foods.read_foods_from_json_file('tests/test_foods.json')
    assert foods.len() == 2
    str_json_foods_read = foods.foods_to_json_str()
    assert str_json_foods_written == str_json_foods_read
