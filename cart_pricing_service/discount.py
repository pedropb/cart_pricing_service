from math import floor

from cart_pricing_service.cart import Cart, DiscountPolicy
from cart_pricing_service.inventory import APPLES, GRAPES


class ApplesDiscount(DiscountPolicy):
    def get_discount(self, cart: Cart) -> int:
        apple_count = cart.get_item_count(APPLES)
        if apple_count >= 2:
            return floor(apple_count * APPLES.price * 0.2)
        else:
            return 0


class GrapesDiscount(DiscountPolicy):
    def get_discount(self, cart: Cart) -> int:
        buy_one_get_one_free_count = cart.get_item_count(GRAPES) // 2
        return buy_one_get_one_free_count * GRAPES.price
