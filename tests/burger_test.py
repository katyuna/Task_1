from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


class TestBurger:
    #булочка устанавливается
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    # ингредиент добавляется в список
    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    # удаляется ингредиент по индексу
    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        sauce = Mock()
        salat = Mock()
        burger.add_ingredient(sauce)
        burger.add_ingredient(salat)

        burger.remove_ingredient(0)

        assert burger.ingredients == [salat]

    # ингредиент переносится
    def test_move_ingredient_changes_order(self):
        burger = Burger()
        sauce = Mock()
        salat = Mock()
        sausage = Mock()
        burger.add_ingredient(sauce)
        burger.add_ingredient(salat)
        burger.add_ingredient(sausage)

        # переносим ингредиент с индексом 0 в конец
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [salat, sausage, sauce]

    # цена бургера = цена булочки * 2  + цена всех ингредиентов
    # три случая: без ингредиентов, с одним и с несколькими
    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_price', [
        (10, [], 20),
        (10, [5], 25),
        (10, [5, 2.5], 27.5),
    ])
    def test_get_price_returns_buns_and_ingredients_sum(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    #  чек печатается в нужном формате
    def test_get_receipt_returns_burger_description(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = 'My Bun'
        bun.get_price.return_value = 100
        burger.set_buns(bun)
        ingredient = Mock()
        ingredient.get_type.return_value = 'SAUCE'
        ingredient.get_name.return_value = 'spicy sauce'
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        expected_receipt = (
            '(==== My Bun ====)\n'
            '= sauce spicy sauce =\n'
            '(==== My Bun ====)\n'
            '\n'
            'Price: 250'
        )

        assert burger.get_receipt() == expected_receipt
