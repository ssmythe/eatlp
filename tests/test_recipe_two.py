from src.items import Items
from src.recipe import Recipe

import pytest

test_items_file = 'tests/test_items_2.json'
test_recipe_file = 'tests/test_recipe_black_beans_and_onions.json'


@ pytest.fixture
def items():
    return Items()


@ pytest.fixture
def recipe():
    return Recipe()


def test_carb_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(test_recipe_file)
    assert recipe.carb_per_ingredient_to_list(items) == [34.1, 1, 1.4]


def test_total_carb_per_recipe_serving(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(
        test_recipe_file)
    assert recipe.total_carb_per_recipe_serving(items) == 37


def test_fat_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(
        test_recipe_file)
    assert recipe.fat_per_ingredient_to_list(items) == [1.6, 0.0, 0.0]


def test_total_fat_per_recipe_serving(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(
        test_recipe_file)
    assert recipe.total_fat_per_recipe_serving(items) == 2


# def test_protein_per_recipes_to_list(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.protein_per_ingredient_to_list(items) == [5, 2]


# def test_total_protein_per_recipe_serving(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.total_protein_per_recipe_serving(items) == 7


# def test_sodium_per_recipes_to_list(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.sodium_per_ingredient_to_list(items) == [75, 125]


# def test_total_sodium_per_recipe_serving(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.total_sodium_per_recipe_serving(items) == 200


# def test_kcal_per_recipes_to_list(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.kcal_per_ingredient_to_list(items) == [85, 69]


# def test_total_kcal_per_recipe_serving(items, recipe):
#     items.add_items_from_json_file(test_items_file)
#     recipe.set_recipe_from_json_file(
#         test_recipe_file)
#     assert recipe.total_kcal_per_recipe_serving(items) == 154


def test_price_per_recipes_to_list(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(
        test_recipe_file)
    assert recipe.price_per_ingredient_to_list(items) == [0.24, 0.45, 0.12]


def test_total_price_per_recipe_serving(items, recipe):
    items.add_items_from_json_file(test_items_file)
    recipe.set_recipe_from_json_file(
        test_recipe_file)
    assert recipe.total_price_per_recipe_serving(items) == 0.81
