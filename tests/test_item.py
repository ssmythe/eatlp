from src.item import Item

import pytest


@pytest.fixture
def item():
    return Item()


def test_constructor(item):
    assert isinstance(item, Item)
