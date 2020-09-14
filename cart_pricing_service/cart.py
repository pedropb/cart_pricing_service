from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import Dict, List

from cart_pricing_service.inventory import Item


class DiscountPolicy(metaclass=abc.ABCMeta):
    def get_discount(self, cart: Cart) -> int:
        return 0


class Cart:
    items: Dict[str, CartItem]

    def get_price(self, discounts: List[DiscountPolicy]) -> int:
        price_before_discount = sum(
            cart_item.item.price * cart_item.quantity
            for cart_item in self.items.values()
        )
        discount = sum(policy.get_discount(self) for policy in discounts)
        return price_before_discount - discount

    def get_item_count(self, item: Item) -> int:
        return self.items[item.name].quantity if item.name in self.items else 0

    def add_item(self, item: Item, quantity: int = 1) -> Cart:
        if item.name in self.items:
            quantity += self.items[item.name].quantity

        self.items[item.name] = CartItem(item, quantity)

        return self

    def remove_item(self, item: Item, quantity: int = None) -> Cart:
        if item.name in self.items:
            current_quantity = self.items[item.name].quantity
            if quantity is None or current_quantity == 1:
                del self.items[item.name]
            else:
                self.items[item.name] = CartItem(item, current_quantity - quantity)
        return self

    @staticmethod
    def from_list(list_: List[List]) -> Cart:
        cart = Cart()
        for item in list_:
            cart.add_item(Item.from_list(item), item[2])

        return cart


@dataclass(frozen=True)
class CartItem:
    item: Item
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("Quantity has to be greater than 0")
