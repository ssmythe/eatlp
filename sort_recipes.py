#!/usr/bin/env python3

from src.recipes import Recipes

import pytest


pytestmark = pytest.mark.skip


recipes = Recipes()
recipes.set_recipes_from_json_file('data/recipes.json')
recipes.write_recipes_to_json_file('data/recipes.json')
