from src.recipe import Recipe

import pytest

dict_toast_with_hummus = {
    'name': 'toast with hummus',
    'servings_per_recipe': 1,
    'serving_size': '1 slice (? g)',
    'ingredients': {
        'ezekiel bread': 1,
        'sabra roasted red pepper hummus': 1
    }
}

json_toast_with_hummus = '''
{
    "toast with hummus": {
        "servings": 1,
        "servings per recipe": 1,
        "serving size": "1 slice (? g)",
        "ingredients": {
            "ezekiel bread": 1,
            "sabra roasted red pepper hummus": 1
        }
    }
}
'''


@ pytest.fixture
def recipe():
    return Recipe()


def test_constructor(recipe):
    assert isinstance(recipe, Recipe)


def test_set_name(recipe):
    name = 'toast with hummus'
    recipe.set_name(name)
    assert recipe.name == name


def test_set_servings_per_recipe(recipe):
    servings_per_recipe = 1
    recipe.set_servings_per_recipe(servings_per_recipe)
    assert recipe.servings_per_recipe == servings_per_recipe


def test_set_serving_size(recipe):
    serving_size = '1 slice (? g)'
    recipe.set_serving_size(serving_size)
    assert recipe.serving_size == serving_size


def test_set_ingredients(recipe):
    ingredients = {'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}
    recipe.set_ingredients(ingredients)
    assert recipe.ingredients == ingredients


def test_set_recipe_from_dict(recipe):
    recipe.set_recipe_from_dict(dict_toast_with_hummus)
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}


def test_set_item_from_json_str(recipe):
    recipe.set_recipe_from_json_str(json_toast_with_hummus)
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}


def test_set_item_from_json_file(recipe):
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}
