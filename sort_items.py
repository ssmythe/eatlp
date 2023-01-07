#!/usr/bin/env python

from src.items import Items
from src.user import User

import pytest


pytestmark = pytest.mark.skip

user = User()
user.read_user_from_json_file('user.json')
data_dir = user.dict_of_user['data_dir']

items = Items()
items.add_items_from_json_file(data_dir + '/items.json')
items.write_items_to_json_file(data_dir + '/items.json')
