#!/usr/bin/env python3

from src.items import Items

import pytest


pytestmark = pytest.mark.skip


items = Items()
items.add_items_from_json_file('data/items.json')
items.write_items_to_json_file('data/items.json')
