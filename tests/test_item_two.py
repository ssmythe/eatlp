from src.item import Item

import pytest


@pytest.fixture
def item():
    return Item()


def test_set_item_from_json_file(item):
    item.set_item_from_json_file('tests/test_item_almondmilk.json')
    assert item.name == 'almondmilk'
    assert item.carb_per_serving == 1
    assert item.fat_per_serving == 2.5
    assert item.protein_per_serving == 1
