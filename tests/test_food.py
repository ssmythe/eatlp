from src.food import Food
from src.recipe import Recipe

import pytest


@pytest.fixture
def food():
    return Food()


@pytest.fixture
def recipe():
    return Recipe()


def test_constructor(food):
    assert isinstance(food, Food)


def test_recipe_to_food(recipe, food):
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    food.recipe_to_food(recipe, food)
    assert food.name == 'toast with hummus'
    assert food.servings_per_food == 1
    assert food.serving_size == '1 slice (? g)'
    assert food.min_servings == 0
    assert food.max_servings == 1
