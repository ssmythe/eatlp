from src.items import Items
from src.recipe import Recipe

import pytest

test_items_file = 'tests/test_item_almondmilk.json'
test_recipe_file = 'tests/test_recipe_almondmilk.json'


@ pytest.fixture
def items():
    return Items()


@ pytest.fixture
def recipe():
    return Recipe()


def test_price_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(test_recipe_file)
    assert recipe.fat_per_ingredient_to_list(items) == [2.5]


def test_total_price_per_recipe_serving(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(test_recipe_file)
    assert recipe.total_fat_per_recipe_serving(items) == 2.5
