from cart_pricing_service.cart import Cart, DiscountPolicy
from cart_pricing_service.inventory import APPLES, BANANAS, GRAPES


class TestCart:
    def test_from_list(self):
        cart = Cart.from_list([[APPLES, 1], [GRAPES, 2], [BANANAS, 3]])

        assert cart.get_item_count(APPLES) == 1
        assert cart.get_item_count(GRAPES) == 2
        assert cart.get_item_count(BANANAS) == 3
        assert cart.get_item_count() == 6

    def test_from_empty_list(self):
        cart = Cart.from_list([])

        assert cart.get_item_count() == 0

    def test_get_price(self):
        cart = Cart.from_list([[APPLES, 1]])

        class MockDiscount(DiscountPolicy):
            def get_discount(self, cart: Cart) -> int:
                return 100  # flat 1 dollar discount

        assert cart.get_price([MockDiscount()]) == APPLES.price - 100
        assert cart.get_price() == APPLES.price
