from src.item import Item

import pytest


@pytest.fixture
def item():
    return Item()


def test_constructor(item):
    assert isinstance(item, Item)


def test_set_name(item):
    name = "ezekiel bread"
    item.set_name(name)
    assert item.name == name


def test_set_brand_name(item):
    brand_name = "Food For Life Ezekiel 4:9 Organic Bread Sprouted Whole Grain - 24 Oz"
    item.set_brand_name(brand_name)
    assert item.brand_name == brand_name


def test_set_price(item):
    price = 7.79
    item.set_price(price)
    assert item.price == price


def test_set_servings_per_container(item):
    servings_per_container = 20
    item.set_servings_per_container(servings_per_container)
    assert item.servings_per_container == servings_per_container


def test_set_serving_size(item):
    serving_size = "1 slice (34g)"
    item.set_serving_size(serving_size)
    assert item.serving_size == serving_size


def test_set_kcal_per_serving(item):
    kcal_per_serving = 80
    item.set_kcal_per_serving(kcal_per_serving)
    assert item.kcal_per_serving == kcal_per_serving


def test_set_carb_per_serving(item):
    carb_per_serving = 0.5
    item.set_carb_per_serving(carb_per_serving)
    assert item.carb_per_serving == carb_per_serving


def test_set_fat_per_serving(item):
    fat_per_serving = 0.5
    item.set_fat_per_serving(fat_per_serving)
    assert item.fat_per_serving == fat_per_serving


def test_set_protein_per_serving(item):
    protein_per_serving = 0.5
    item.set_protein_per_serving(protein_per_serving)
    assert item.protein_per_serving == protein_per_serving


def test_set_sodium_per_serving(item):
    sodium_per_serving = 0.5
    item.set_sodium_per_serving(sodium_per_serving)
    assert item.sodium_per_serving == sodium_per_serving


def test_cost_per_serving(item):
    name = "ezekiel bread"
    servings_per_container = 20
    price = 7.79
    item.set_name(name)
    item.set_price(price)
    item.set_servings_per_container(servings_per_container)
    assert item.cost_per_serving() == 0.39
