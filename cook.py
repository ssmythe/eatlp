#!/usr/bin/env python3

from src.foods import Foods
from src.recipes import Recipes
from src.items import Items
from src.user import User

items = Items()
recipes = Recipes()
foods = Foods()
user = User()

user.read_user_from_json_file('user.json')
data_dir = user.dict_of_user['data_dir']

items_file = data_dir + '/items.json'
recipes_file = data_dir + '/recipes.json'
foods_file = data_dir + '/foods.json'

items.add_items_from_json_file(items_file)
recipes.set_recipes_from_json_file(recipes_file)
foods.recipes_to_foods(items, recipes)
foods.write_foods_to_json_file(foods_file)
