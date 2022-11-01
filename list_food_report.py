#!/usr/bin/env python3

# TODO use cli argument to designate key to sort by

from src.bmi import BMI
from src.foods import Foods
from src.food import Food
from src.randomfoods import RandomFoods
from src.user import User
from src.msje import *

import argparse
import pytest
import sys


pytestmark = pytest.mark.skip

parser = argparse.ArgumentParser()
parser.version = '1.0.0'
parser.add_argument('-a', '--all', action='store_true', help='used to iterate through all keys')
parser.add_argument('-k', '--key', default='price', help='keys are kcal, carb, fat, protein, sodium, fiber, or price')
args = parser.parse_args()

# validate key value
acceptable_keys = ['kcal', 'carb', 'fat', 'protein', 'sodium', 'fiber', 'price']
if args.key not in acceptable_keys:
    print(f"Error: {args.key} not in {acceptable_keys}")
    sys.exit(1)

foods = Foods()
foods.read_foods_from_json_file('data/foods.json')

food_and_key_dict = {}


# Build list of keys to iterate
if args.all:
    keys = acceptable_keys
else:
    keys = [args.key]

# Iterate keys
for iterate_key in keys:
    print(f"Sorted by {iterate_key.capitalize()}")
    print('-' * 110)

    # Build dict of food name and price
    key = iterate_key + "_per_serving"
    for name in foods.dict_of_foods.keys():
        food_and_key_dict[name] = foods.dict_of_foods[name][key]

    # List values
    sorted_keys = dict(sorted(food_and_key_dict.items(), key=lambda item: item[1]))
    for name in sorted_keys.keys():
        food = foods.dict_of_foods[name]
        kcal = food['kcal_per_serving']
        carb = food['carb_per_serving']
        fat = food['fat_per_serving']
        fiber = food['fiber_per_serving']
        protein = food['protein_per_serving']
        sodium = food['sodium_per_serving']
        price = food['price_per_serving']
        print("%-30s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d, fiber %4d, $%6.2f" %
            (name, kcal, carb, fat, protein, sodium, fiber, price))

    print("\n")