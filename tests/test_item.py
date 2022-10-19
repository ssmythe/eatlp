from src.item import Item

import pytest


json_ezekiel_bread = '''
{
  "ezekiel bread": {
    "store": "Safeway",
    "store product name": "Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz",
    "serving size": "1 slice (34g)",
    "servings per container": 20,
    "price": 7.79,
    "carb": 15,
    "fat": 0.5,
    "protein": 5,
    "sodium": 75
  }
}
'''


dict_ezekiel_bread = {
    'name': 'ezekiel bread',
    'store_name': 'Safeway',
    'store_product_name': 'Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz',
    'price': 7.79,
    'servings_per_container': 20,
    'serving_size': '1 slice (34g)',
    'carb_per_serving': 15,
    'fat_per_serving': 0.5,
    'protein_per_serving': 5,
    'sodium_per_serving': 75
}


@pytest.fixture
def item():
    return Item()


def test_constructor(item):
    assert isinstance(item, Item)


def test_set_name(item):
    name = 'ezekiel bread'
    item.set_name(name)
    assert item.name == name


def test_set_store_name(item):
    store_name = 'Safeway'
    item.set_store_name(store_name)
    assert item.store_name == store_name


def test_set_store_product_name(item):
    store_product_name = 'Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz'
    item.set_store_product_name(store_product_name)
    assert item.store_product_name == store_product_name


def test_set_price(item):
    price = 7.79
    item.set_price(price)
    assert item.price == price


def test_set_servings_per_container(item):
    servings_per_container = 20
    item.set_servings_per_container(servings_per_container)
    assert item.servings_per_container == servings_per_container


def test_set_serving_size(item):
    serving_size = '1 slice (34g)'
    item.set_serving_size(serving_size)
    assert item.serving_size == serving_size


def test_set_carb_per_serving(item):
    carb_per_serving = 15
    item.set_carb_per_serving(carb_per_serving)
    assert item.carb_per_serving == carb_per_serving


def test_set_fat_per_serving(item):
    fat_per_serving = 0.5
    item.set_fat_per_serving(fat_per_serving)
    assert item.fat_per_serving == fat_per_serving


def test_set_protein_per_serving(item):
    protein_per_serving = 5
    item.set_protein_per_serving(protein_per_serving)
    assert item.protein_per_serving == protein_per_serving


def test_kcal_per_serving(item):
    carb_per_serving = 15
    item.set_carb_per_serving(carb_per_serving)
    fat_per_serving = 0.5
    item.set_fat_per_serving(fat_per_serving)
    protein_per_serving = 5
    item.set_protein_per_serving(protein_per_serving)
    assert item.kcal_per_serving() == 84.5


def test_set_sodium_per_serving(item):
    sodium_per_serving = 75
    item.set_sodium_per_serving(sodium_per_serving)
    assert item.sodium_per_serving == sodium_per_serving


def test_price_per_serving(item):
    name = 'ezekiel bread'
    servings_per_container = 20
    price = 7.79
    item.set_name(name)
    item.set_price(price)
    item.set_servings_per_container(servings_per_container)
    assert item.price_per_serving() == 0.39


def test_set_item_from_dict(item):
    item.set_item_from_dict(dict_ezekiel_bread)
    assert item.name == 'ezekiel bread'
    assert item.store_product_name == 'Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz'
    assert item.price == 7.79
    assert item.servings_per_container == 20
    assert item.serving_size == '1 slice (34g)'
    assert item.carb_per_serving == 15
    assert item.fat_per_serving == 0.5
    assert item.protein_per_serving == 5
    assert item.sodium_per_serving == 75
    assert item.kcal_per_serving() == 84.5


def test_set_item_from_json_str(item):
    item.set_item_from_json_str(json_ezekiel_bread)
    assert item.name == 'ezekiel bread'
    assert item.store_product_name == 'Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz'
    assert item.price == 7.79
    assert item.servings_per_container == 20
    assert item.serving_size == '1 slice (34g)'
    assert item.carb_per_serving == 15
    assert item.fat_per_serving == 0.5
    assert item.protein_per_serving == 5
    assert item.sodium_per_serving == 75
    assert item.price_per_serving() == 0.39
    assert item.kcal_per_serving() == 84.5


def test_set_item_from_json_file(item):
    item.set_item_from_json_file('tests/test_item_ezekiel_bread.json')
    assert item.name == 'ezekiel bread'
    assert item.store_product_name == 'Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz'
    assert item.price == 7.79
    assert item.servings_per_container == 20
    assert item.serving_size == '1 slice (34g)'
    assert item.carb_per_serving == 15
    assert item.fat_per_serving == 0.5
    assert item.protein_per_serving == 5
    assert item.sodium_per_serving == 75
    assert item.price_per_serving() == 0.39
    assert item.kcal_per_serving() == 84.5
