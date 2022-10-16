from src.item import Item
from src.items import Items

import pytest


@pytest.fixture
def items():
    return Items()


def test_constructor(items):
    assert isinstance(items, Items)
    assert items.list_of_items == []


def test_add_items_from_json_file(items):
    items.add_items_from_json_file('tests/test_items.json')
    assert items.len() == 2
    assert items.list_of_items_names() == [
        'ezekiel bread',
        'sabra roasted red pepper hummus'
    ]
