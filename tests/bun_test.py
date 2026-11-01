import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', ['My Bun', ''])
    def test_get_name_returns_name_from_constructor(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    # Цена бывает целой и дробной (тип float), проверим оба варианта и ноль.
    @pytest.mark.parametrize('price', [10, 10.99, 0])
    def test_get_price_returns_price_from_constructor(self, price):
        bun = Bun('My Bun', price)

        assert bun.get_price() == price
