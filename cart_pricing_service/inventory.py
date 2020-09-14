from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Item:
    name: str
    price: int

    @staticmethod
    def from_list(list_: List) -> Item:
        return Item(list_[0], list_[1])


APPLES = Item("Apples", 700)
GRAPES = Item("Grapes", 1500)
BANANAS = Item("Bananas", 300)
