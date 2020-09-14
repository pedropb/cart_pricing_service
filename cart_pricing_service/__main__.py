import sys

from cart_pricing_service.cart_pricing_service import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
