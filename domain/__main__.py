from domain.cart import Cart
from domain.discount import ApplesDiscount, GrapesDiscount
from domain.inventory import APPLES, BANANAS, GRAPES

if __name__ == "__main__":
    apple_count = int(input(f"How many {APPLES.name} (${APPLES.price/100:.2f})? "))
    banana_count = int(input(f"How many {BANANAS.name} (${BANANAS.price/100:.2f})? "))
    grape_count = int(input(f"How many {GRAPES.name} (${GRAPES.price/100:.2f})? "))

    cart = Cart.from_list(
        [[APPLES, apple_count], [BANANAS, banana_count], [GRAPES, grape_count]]
    )

    print("----------------------------")
    print(
        f"Your cart total is: ${cart.get_price([ApplesDiscount(), GrapesDiscount()]) / 100 :.2f}"
    )
