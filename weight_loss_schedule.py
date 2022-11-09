#!/usr/bin/env python3

# TODO add kg weight output as well

from src.user import *
from src.bmi import *
from src.msje import *

import datetime


user = User()
user.read_user_from_json_file('user.json')
weight_loss_per_week_lbs = user.dict_of_user['weight_loss_per_week_lbs']
height_inches = user.dict_of_user['height_inches']
msje_activity_factor = user.dict_of_user['msje_activity_factor']

# start
start_weight_lbs = user.dict_of_user['start_weight_lbs']
start_weight_kg = BMI.lbs_to_kg(start_weight_lbs)
start_weight_date = user.dict_of_user['start_weight_date']
start_bmi = round(BMI.height_inches_weight_lbs_to_bmi(
    height_inches, start_weight_lbs), 1)

# current
current_weight_lbs = user.dict_of_user['current_weight_lbs']
current_weight_kg = BMI.lbs_to_kg(current_weight_lbs)
current_weight_date = datetime.date.today()
current_bmi = round(BMI.height_inches_weight_lbs_to_bmi(
    height_inches, current_weight_lbs), 1)
start_current_weight_lbs_diff = round(start_weight_lbs - current_weight_lbs, 1)

# target
target_weight_lbs = BMI.height_inches_bmi_to_weight_lbs(
    user.dict_of_user['height_inches'], user.dict_of_user['target_bmi'])
target_weight_kg = BMI.lbs_to_kg(target_weight_lbs)
current_target_weight_lbs_diff = round(
    current_weight_lbs - target_weight_lbs, 1)
start_target_weight_lbs_diff = round(
    start_weight_lbs - target_weight_lbs, 1)
num_of_weeks_remaining = current_target_weight_lbs_diff / weight_loss_per_week_lbs
num_of_days_remaining = int(num_of_weeks_remaining * 7)
target_weight_date = current_weight_date + \
    datetime.timedelta(days=num_of_days_remaining)
target_bmi = user.dict_of_user['target_bmi']

today_max_kcal = MSJE.target_kcal_user_target_weight_lbs(
    user, target_weight_lbs)
current_percent_lost_lbs = round(
    (start_current_weight_lbs_diff / start_target_weight_lbs_diff) * 100, 1)


print(f"Today's max kcal:    {today_max_kcal} kcal ({msje_activity_factor})\n")

print(
    f"Start weight date:   {start_weight_date} ({start_weight_lbs} lbs/{start_weight_kg} kg, {start_bmi} bmi, {start_current_weight_lbs_diff} of {start_target_weight_lbs_diff} lbs lost)")
print(
    f"Current weight date: {current_weight_date} ({current_weight_lbs} lbs/{current_weight_kg} kg, {current_bmi} bmi, {current_percent_lost_lbs}% of target weight lost)")
print(
    f"Target weight date:  {target_weight_date} ({target_weight_lbs} lbs/{target_weight_kg} kg, {target_bmi} bmi, {current_target_weight_lbs_diff} lbs to go, {num_of_days_remaining} days remaining)")
