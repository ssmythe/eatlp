#!/usr/bin/env python3

from src.foods import Foods
from src.recipes import Recipes
from src.items import Items

items = Items()
recipes = Recipes()
foods = Foods()

items_file = 'data/items.json'
recipes_file = 'data/recipes.json'
foods_file = 'data/foods.json'

items.add_items_from_json_file(items_file)
recipes.set_recipes_from_json_file(recipes_file)
foods.recipes_to_foods(items, recipes)
foods.write_foods_to_json_file(foods_file)
