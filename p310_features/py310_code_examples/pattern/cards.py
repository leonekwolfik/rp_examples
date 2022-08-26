# pattern/cards.py
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str

def is_red(card):
    match card:
        case Card(suit=suit) if suit in "♢♡":
            return True
        case Card():
            return False
        case _:
            raise ValueError(f"{card} is not a Card object")


print(is_red(Card("2", "♡")))

print(is_red(Card("K", "♣")))

is_red('cart')