from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = 'brioche'
    bun.get_price.return_value = 12.5
    return bun


@pytest.fixture
def ingredients():
    sauce = Mock(spec=Ingredient)
    sauce.get_name.return_value = 'mustard'
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_price.return_value = 3.5

    filling = Mock(spec=Ingredient)
    filling.get_name.return_value = 'cutlet'
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_price.return_value = 25
    return [sauce, filling]


def test_set_buns_assigns_selected_bun(bun):
    burger = Burger()
    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_appends_in_order(ingredients):
    burger = Burger()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    assert burger.ingredients == ingredients


def test_remove_ingredient_removes_selected_layer(ingredients):
    burger = Burger()
    burger.ingredients = ingredients.copy()
    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredients[1]]


def test_move_ingredient_preserves_other_layers(ingredients):
    burger = Burger()
    sauce, filling = ingredients
    cheese = Mock(spec=Ingredient)
    burger.ingredients = [sauce, filling, cheese]
    burger.move_ingredient(2, 0)

    assert burger.ingredients == [cheese, sauce, filling]


@pytest.mark.parametrize('layer_count, expected_price', [(0, 25.0), (2, 53.5)])
def test_price_includes_both_bun_halves_and_every_layer(
    bun, ingredients, layer_count, expected_price
):
    burger = Burger()
    burger.bun = bun
    burger.ingredients = ingredients[:layer_count]

    assert burger.get_price() == expected_price


def test_receipt_shows_layers_in_order_and_total(bun, ingredients):
    burger = Burger()
    burger.bun = bun
    burger.ingredients = ingredients

    assert burger.get_receipt() == (
        '(==== brioche ====)\n'
        '= sauce mustard =\n'
        '= filling cutlet =\n'
        '(==== brioche ====)\n\n'
        'Price: 53.5'
    )
