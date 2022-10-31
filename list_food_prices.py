#!/usr/bin/env python3

# TODO use cli argument to designate key to sort by

from src.bmi import BMI
from src.foods import Foods
from src.food import Food
from src.randomfoods import RandomFoods
from src.user import User
from src.msje import *

import pytest


pytestmark = pytest.mark.skip


foods = Foods()
foods.read_foods_from_json_file('data/foods.json')

food_and_price_dict = {}

# Build dict of food name and price
for name in foods.dict_of_foods.keys():
    food_and_price_dict[name] = foods.dict_of_foods[name]['price_per_serving']


for name, price in sorted(food_and_price_dict.items(), key=lambda item: item[1]):
    food = foods.dict_of_foods[name]
    kcal = food['kcal_per_serving']
    kcal_times_servings = kcal
    carb = food['carb_per_serving']
    carb_times_servings = carb
    fat = food['fat_per_serving']
    fat_times_servings = fat
    fiber = food['fiber_per_serving']
    fiber_times_servings = fiber
    protein = food['protein_per_serving']
    protein_times_servings = protein
    sodium = food['sodium_per_serving']
    sodium_times_servings = sodium
    price_times_servings = price
    print("%-30s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d, fiber %4d, $%6.2f" %
          (name, kcal_times_servings, carb_times_servings, fat_times_servings, protein_times_servings, sodium_times_servings, fiber_times_servings, price_times_servings))
