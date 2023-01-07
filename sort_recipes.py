#!/usr/bin/env python

from src.recipes import Recipes
from src.user import User

import pytest


pytestmark = pytest.mark.skip

user = User()
user.read_user_from_json_file('user.json')
data_dir = user.dict_of_user['data_dir']

recipes = Recipes()
recipes.set_recipes_from_json_file(data_dir + '/recipes.json')
recipes.write_recipes_to_json_file(data_dir + '/recipes.json')
