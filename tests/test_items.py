from src.item import Item
from src.items import Items

import pytest


@pytest.fixture
def items():
    return Items()


def test_constructor(items):
    assert isinstance(items, Items)
    assert items.dict_of_items == {}


def test_add_items_from_json_file(items):
    items.add_items_from_json_file('tests/test_items.json')
    assert items.len() == 3
    assert items.list_of_items_names() == [
        'chao slices',
        'ebread',
        'sabra roasted red pepper hummus'
    ]


def test_write_items_to_json_file(items):
    items.add_items_from_json_file('tests/test_items_unsorted.json')
    items.write_items_to_json_file('tests/test_items_sorted.json')
    items.add_items_from_json_file('tests/test_items_sorted.json')
    assert items.len() == 3
    assert items.list_of_items_names() == [
        'chao slices',
        'ebread',
        'sabra roasted red pepper hummus'
    ]


def test_get_item_from_items_by_name(items):
    items.add_items_from_json_file('tests/test_items.json')
    item = Item()
    item.set_item_from_json_file('tests/test_item_ezekiel_bread.json')
    assert item.name == 'ebread'
    assert items.get_item_from_items_by_name('ebread').name == item.name
