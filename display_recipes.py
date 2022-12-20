#!/usr/bin/env python3

from src.item import Item
from src.items import Items
from src.recipes import Recipes
from src.foods import Foods
from src.user import User

import pytest


pytestmark = pytest.mark.skip

user = User()
user.read_user_from_json_file('user.json')
data_dir = user.dict_of_user['data_dir']

items = Items()
items.add_items_from_json_file(data_dir + '/items.json')

recipes = Recipes()
recipes.set_recipes_from_json_file(data_dir + '/recipes.json')

foods = Foods()
foods.read_foods_from_json_file(data_dir + '/foods.json')

for recipe_key, recipe in recipes.dict_of_recipes.items():
    servings_per_recipe = recipes.dict_of_recipes[recipe_key].dict_of_recipe['servings_per_recipe']
    serving_size = recipes.dict_of_recipes[recipe_key].dict_of_recipe['serving_size']
    print (f"Recipe: {recipe_key} (makes {servings_per_recipe} servings of {serving_size})")
    print('-' * 114)

    food = foods.dict_of_foods[recipe_key]
    kcal = food['kcal_per_serving']
    carb = food['carb_per_serving']
    fat = food['fat_per_serving']
    fiber = food['fiber_per_serving']
    protein = food['protein_per_serving']
    sodium = food['sodium_per_serving']
    price = food['price_per_serving']
    priceperkcal = food['price_per_kcal_per_serving'] * 100
    cent_symbol = chr(162)
    print("%-30s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d, fiber %4d, $%6.2f, %2.2f%s" %
        (recipe_key, kcal, carb, fat, protein, sodium, fiber, price, priceperkcal, cent_symbol))

    print('-' * 114)
    for ingredient, count in recipe.dict_of_recipe['ingredients'].items():
        item = items.dict_of_items[ingredient]
        item_serving_size = item.dict_of_item['serving_size']
        print("%2dx %s (%s per serving)" % (count, ingredient, item_serving_size))

    print('-' * 114)
    print('\n')