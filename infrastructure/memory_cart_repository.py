from typing import Dict

from cart_pricing_service.cart import Cart, CartId, CartRepository


class NotFoundError(Exception):
    pass


class MemoryCartRepository(CartRepository):
    storage: Dict[CartId, Cart]

    def __init__(self) -> None:
        super().__init__()
        self.storage = {}

    def save(self, cart: Cart) -> Cart:
        self.storage[cart.id] = cart
        return cart

    def fetch(self, cart_id: CartId) -> Cart:
        if cart_id not in self.storage:
            raise NotFoundError()

        return self.storage[cart_id]
