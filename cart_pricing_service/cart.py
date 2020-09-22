from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID, uuid4

from cart_pricing_service.inventory import Item

CartId = UUID


class Cart:
    id: CartId
    items: Dict[str, CartItem]

    def __init__(self) -> None:
        self.id = uuid4()
        self.items = {}

    def get_price(self, discounts: List[DiscountPolicy] = None) -> int:
        if discounts is None:
            discounts = []

        price_before_discount = sum(
            cart_item.item.price * cart_item.quantity
            for cart_item in self.items.values()
        )
        discount = sum(policy.get_discount(self) for policy in discounts)
        return price_before_discount - discount

    def get_item_count(self, item: Item = None) -> int:
        if item is None:
            return sum(cart_item.quantity for cart_item in self.items.values())
        else:
            return self.items[item.name].quantity if item.name in self.items else 0

    def add_item(self, item: Item, quantity: int = 1) -> Cart:
        if item.name in self.items:
            quantity += self.items[item.name].quantity

        self.items[item.name] = CartItem(item, quantity)

        return self

    @staticmethod
    def from_list(list_: List[List]) -> Cart:
        cart = Cart()
        for item in list_:
            cart.add_item(*item)

        return cart


class DiscountPolicy(ABC):
    @abstractmethod
    def get_discount(self, cart: Cart) -> int:
        return 0


class CartRepository(ABC):
    @abstractmethod
    def save(self, cart: Cart) -> Cart:
        pass

    def fetch(self, cart_id: CartId) -> Cart:
        pass


@dataclass(frozen=True)
class CartItem:
    item: Item
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("Quantity has to be greater than 0")
