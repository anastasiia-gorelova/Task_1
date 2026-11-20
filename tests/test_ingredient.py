import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    'ingredient_type, name, price',
    [
        (INGREDIENT_TYPE_SAUCE, 'mustard', 3.5),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 25),
    ],
)
def test_ingredient_returns_its_type_name_and_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert (ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) == (
        ingredient_type, name, price
    )
