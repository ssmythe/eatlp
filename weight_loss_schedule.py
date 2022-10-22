#!/usr/bin/env python3

from src.user import *
from src.bmi import *

import datetime


user = User()
user.read_user_from_json_file('user.json')
weight_loss_per_week_lbs = user.dict_of_user['weight_loss_per_week_lbs']
start_weight_date = user.dict_of_user['start_weight_date']
current_weight_lbs = user.dict_of_user['current_weight_lbs']
current_weight_date = datetime.date.today()

target_weight_lbs = BMI.height_inches_bmi_to_weight_lbs(
    user.dict_of_user['height_inches'], user.dict_of_user['target_bmi'])
current_target_weight_lbs_diff = current_weight_lbs - target_weight_lbs

num_of_weeks_remaining = current_target_weight_lbs_diff / weight_loss_per_week_lbs
num_of_days_remaining = int(num_of_weeks_remaining * 7)

target_weight_date = current_weight_date + \
    datetime.timedelta(days=num_of_days_remaining)

print(f"Start weight date:   {start_weight_date}")
print(f"Current weight date: {current_weight_date}")
print(
    f"Target weight date:  {target_weight_date} ({num_of_days_remaining} days remaining)")
