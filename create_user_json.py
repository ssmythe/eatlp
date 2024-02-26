#!/usr/bin/env python

from src.user import User
from src.msje import MSJE


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
kcal_adjust = int(input("Kcal adjust: "))
max_sodium = int(input("Maximum sodium: "))
max_num_of_menus = int(input("How many menus to generate: "))
sex = input("Sex (male|female): ")
start_weight_date = input("Start weight date (yyyy-mm-dd): ")
start_weight_lbs = float(input("Start weight in lbs: "))
target_bmi = float(input("Target BMI: "))


user.dict_of_user['msje_activity_factor'] = msje_activity_factor
user.dict_of_user['current_age'] = current_age
user.dict_of_user['height_inches'] = height_inches
user.dict_of_user['current_weight_lbs'] = current_weight_lbs
user.dict_of_user['weight_loss_per_week_lbs'] = weight_loss_per_week_lbs
user.dict_of_user['kcal_adjust'] = kcal_adjust
user.dict_of_user['max_sodium'] = max_sodium
user.dict_of_user['max_num_of_menus'] = max_num_of_menus
user.dict_of_user['sex'] = sex
user.dict_of_user['start_weight_date'] = start_weight_date
user.dict_of_user['start_weight_lbs'] = start_weight_lbs
user.dict_of_user['target_bmi'] = target_bmi

user.dict_of_user['data_dir'] = 'data'

user.write_user_to_json_file('user.json')
