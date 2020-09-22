from math import floor

from domain.cart import Cart, Discount
from domain.inventory import APPLES, GRAPES


class ApplesDiscount(Discount):
    def __call__(self, cart: Cart) -> int:
        apple_count = cart.get_item_count(APPLES)
        return floor(apple_count * APPLES.price * 0.2) if apple_count >= 2 else 0


class GrapesDiscount(Discount):
    def __call__(self, cart: Cart) -> int:
        buy_one_get_one_free_count = cart.get_item_count(GRAPES) // 2
        return buy_one_get_one_free_count * GRAPES.price
