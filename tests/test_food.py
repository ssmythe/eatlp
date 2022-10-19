from src.food import Food
from src.recipe import Recipe
from src.items import Items

import pytest


@ pytest.fixture
def items():
    return Items()


@pytest.fixture
def food():
    return Food()


@pytest.fixture
def recipe():
    return Recipe()


def test_constructor(food):
    assert isinstance(food, Food)


def test_recipe_to_food(items, recipe, food):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    food.recipe_to_food(items, recipe)
    assert food.name == 'toast with hummus'
    assert food.serving_size == '1 slice (? g)'
    assert food.min_servings == 0
    assert food.max_servings == 1
    assert food.carb_per_serving == 19
    assert food.fat_per_serving == 6
    assert food.protein_per_serving == 7
    assert food.sodium_per_serving == 200
    assert food.kcal_per_serving == 154
    assert food.price_per_serving == 0.86


def test_recipe_to_food(items, recipe, food):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file('tests/test_recipe_toast_with_hummus.json')
    food.recipe_to_food(items, recipe)
    assert food.name == 'toast with hummus'
    assert food.serving_size == '1 slice (? g)'
    assert food.min_servings == 0
    assert food.max_servings == 1
    assert food.carb_per_serving == 19
    assert food.fat_per_serving == 5.5
    assert food.protein_per_serving == 7
    assert food.sodium_per_serving == 200
    assert food.kcal_per_serving == 154
    assert food.price_per_serving == 0.86
