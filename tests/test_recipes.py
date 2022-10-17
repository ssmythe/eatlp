from src.recipe import Recipe
from src.recipes import Recipes

import pytest


@pytest.fixture
def recipes():
    return Recipes()


def test_constructor(recipes):
    assert isinstance(recipes, Recipes)
    assert recipes.dict_of_recipes == {}


def test_set_recipes_from_json_file(recipes):
    recipes.set_recipes_from_json_file('tests/test_recipes.json')
    assert recipes.len() == 2
    assert recipes.list_of_recipes_names() == [
        'toast with chao',
        'toast with hummus',
    ]


def test_get_recipe_from_recipes_by_name(recipes):
    recipes.set_recipes_from_json_file('tests/test_recipes.json')
    recipe = Recipe()
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.name == 'toast with hummus'
    assert recipes.get_recipe_from_recipes_by_name(
        'toast with hummus').name == recipe.name
