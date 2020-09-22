import pytest

from domain.cart import Cart
from infrastructure.memory_cart_repository import MemoryCartRepository, NotFoundError


class TestCartRepository:
    def test_save(self):
        cart = Cart()
        cart_repository = MemoryCartRepository()

        assert cart_repository.save(cart) == cart

    def test_fetch(self):
        cart = Cart()
        cart_repository = MemoryCartRepository()

        with pytest.raises(NotFoundError):
            cart_repository.fetch(cart.id)

        cart_repository.save(cart)
        assert cart_repository.fetch(cart.id) == cart
