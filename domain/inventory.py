from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    price: int


APPLES = Item("Apples", 700)
GRAPES = Item("Grapes", 1500)
BANANAS = Item("Bananas", 300)
