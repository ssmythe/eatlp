#!/usr/bin/env python3

from src.user import *
from src.msje import *

import pytest
pytest.skip(allow_module_level=True)

# TODO refactor current_age to age

user = User()

print("MSJE Activity Levels")
print("-" * 20)
for factor in MSJE.dict_of_activity_factor().keys():
    print(f"{factor}")
print("-" * 20)
msje_activity_factor = input("MSJE activity factor: ")

current_age = int(input("Current age: "))
height_inches = int(input("Current height in inches: "))
current_weight_lbs = float(input("Current weight in lbs: "))
weight_loss_per_week_lbs = int(input("Weight Loss per week in lbs: "))
max_sodium = int(input("Maximum sodium: "))
num_of_menus = int(input("How many menus to generate: "))
sex = input("Sex (male|female): ")
start_weight_date = input("Start weight date (yyyy-mm-dd): ")
start_weight_lbs = input("Start weight in lbs: ")
target_bmi = input("Target BMI: ")


user.dict_of_user['msje_activity_factor'] = msje_activity_factor
user.dict_of_user['current_age'] = current_age
user.dict_of_user['height_inches'] = height_inches
user.dict_of_user['current_weight_lbs'] = current_weight_lbs
user.dict_of_user['weight_loss_per_week_lbs'] = weight_loss_per_week_lbs
user.dict_of_user['max_sodium'] = max_sodium
user.dict_of_user['num_of_menus'] = num_of_menus
user.dict_of_user['sex'] = sex
user.dict_of_user['start_weight_date'] = start_weight_date
user.dict_of_user['start_weight_lbs'] = start_weight_lbs
user.dict_of_user['target_bmi'] = target_bmi


user.write_user_to_json_file('user.json')
