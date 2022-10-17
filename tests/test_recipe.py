from src.items import Items
from src.recipe import Recipe

import pytest

dict_toast_with_hummus = {
    'name': 'toast with hummus',
    'servings_per_recipe': 1,
    'serving_size': '1 slice (? g)',
    'ingredients': {
        'ezekiel bread': 1,
        'sabra roasted red pepper hummus': 1
    },
    'min_servings': 0,
    'max_servings': 1
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
        },
        "min_servings": 0,
        "max_servings": 1
    }
}
'''


@ pytest.fixture
def items():
    return Items()


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


def test_set_min_servings(recipe):
    min_servings = 0
    recipe.set_min_servings(min_servings)
    assert recipe.min_servings == min_servings


def test_set_max_servings(recipe):
    max_servings = 0
    recipe.set_max_servings(max_servings)
    assert recipe.max_servings == max_servings


def test_set_recipe_from_dict(recipe):
    recipe.set_recipe_from_dict(dict_toast_with_hummus)
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}
    assert recipe.min_servings == 0
    assert recipe.max_servings == 1


def test_set_item_from_json_str(recipe):
    recipe.set_recipe_from_json_str(json_toast_with_hummus)
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}
    assert recipe.min_servings == 0
    assert recipe.max_servings == 1


def test_set_recipe_from_json_file(recipe):
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.name == 'toast with hummus'
    assert recipe.servings_per_recipe == 1
    assert recipe.serving_size == '1 slice (? g)'
    assert recipe.ingredients == {
        'ezekiel bread': 1, 'sabra roasted red pepper hummus': 1}
    assert recipe.min_servings == 0
    assert recipe.max_servings == 1


def test_carb_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.carb_per_ingredient_to_list(items) == [15, 4]


def test_total_carb_per_recipe_serving(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.total_carb_per_recipe_serving(items) == 19


def test_fat_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.fat_per_ingredient_to_list(items) == [0.5, 5]


def test_total_fat_per_recipe_serving(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.total_fat_per_recipe_serving(items) == 5.5


def test_protein_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.protein_per_ingredient_to_list(items) == [5, 2]


def test_total_protein_per_recipe_serving(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.total_protein_per_recipe_serving(items) == 7


def test_kcal_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.kcal_per_ingredient_to_list(items) == [85, 69]


def test_total_kcal_per_recipe_serving(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.total_kcal_per_recipe_serving(items) == 154


def test_price_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.price_per_ingredient_to_list(items) == [0.39, 0.47]


def test_total_price_per_recipe_serving(items, recipe):
    items.add_items_from_json_file('tests/test_items.json')
    recipe.set_recipe_from_json_file(
        'tests/test_recipe_toast_with_hummus.json')
    assert recipe.total_price_per_recipe_serving(items) == 0.86
