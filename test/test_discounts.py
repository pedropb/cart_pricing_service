from unittest import mock
from unittest.mock import Mock

import pytest

from cart_pricing_service.cart import Cart
from cart_pricing_service.discount import ApplesDiscount
from cart_pricing_service.inventory import APPLES


class TestDiscounts:
    @pytest.mark.parametrize(
        "apple_count,expected_discount", [(4, APPLES.price * 4 * 0.2), (1, 0), (0, 0)]
    )
    def test_apples_discount(self, apple_count, expected_discount):

        system_under_test = ApplesDiscount()
        cart_mock = mock.create_autospec(Cart)
        cart_mock.get_item_count = Mock(return_value=apple_count)

        assert system_under_test.get_discount(cart_mock) == expected_discount
