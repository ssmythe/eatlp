#!/usr/bin/env python

# TODO check almondmilk and almonds raw sorted by kcal numbers

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
parser.add_argument('-a', '--all', action='store_true',
                    help='used to iterate through all keys')
parser.add_argument('-k', '--key', default='price',
                    help='name keys are kcal, carb, fat, protein, sodium, fiber, or price')
args = parser.parse_args()

# validate key value
acceptable_keys = ['name', 'kcal', 'carb', 'fat',
                   'protein', 'sodium', 'fiber', 'price', 'price_per_kcal']
if args.key not in acceptable_keys:
    print(f"Error: {args.key} not in {acceptable_keys}")
    sys.exit(1)

user = User()
user.read_user_from_json_file('user.json')
data_dir = user.dict_of_user['data_dir']

foods = Foods()
foods.read_foods_from_json_file(data_dir + '/foods.json')

food_and_key_dict = {}


# Build list of keys to iterate
if args.all:
    keys = acceptable_keys
else:
    keys = [args.key]

# Iterate keys
for iterate_key in keys:
    print(f"Sorted by {iterate_key.capitalize()}")
    print('-' * 114)

    if iterate_key == 'name':
        for name in foods.dict_of_foods.keys():
            food_and_key_dict[name] = foods.dict_of_foods[name]
    else:
        # Build dict of food name and price
        key = iterate_key + "_per_serving"
        for name in foods.dict_of_foods.keys():
            food_and_key_dict[name] = foods.dict_of_foods[name][key]

    # List values
    if iterate_key == 'name':
        sorted_keys = dict(sorted(food_and_key_dict.items()))
    else:
        sorted_keys = dict(
            sorted(food_and_key_dict.items(), key=lambda item: item[1]))

    for name in sorted_keys.keys():
        food = foods.dict_of_foods[name]
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
              (name, kcal, carb, fat, protein, sodium, fiber, price, priceperkcal, cent_symbol))

    print("\n")
