#!/usr/bin/env python3

from src.user import *

user = User()
current_weight_lbs = float(input("Current weight in lbs: "))
current_age = int(input("Current age: "))
max_kcal = int(input("Maximum calories: "))
max_sodium = int(input("Maximum sodium: "))
num_of_menus = int(input("How many menus to generate: "))

user.dict_of_user['current_weight_lbs']=current_weight_lbs
user.dict_of_user['current_age']=current_age
user.dict_of_user['max_kcal']=max_kcal
user.dict_of_user['max_sodium']=max_sodium
user.dict_of_user['num_of_menus']=num_of_menus

user.write_user_to_json_file('user.json')
