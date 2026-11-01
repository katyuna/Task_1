import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_returns_type_from_constructor(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'spicy sauce', 10)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('name', ['spicy sauce', ''])
    def test_get_name_returns_name_from_constructor(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 10)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', [10, 10.99, 0])
    def test_get_price_returns_price_from_constructor(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', price)

        assert ingredient.get_price() == price
