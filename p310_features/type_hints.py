from typing import List, Union


def sum_list(numbers: List[Union[float, int]]) -> float:
    pass


def new_sum_list(numbers: list[float | int]) -> float | int:
    pass


user_id = 1234
isinstance(user_id, str | int)


# --------


def get_ace(suit: str | None) -> tuple[str, str]:
    if suit is None:
        suit = 'K'

    return suit, "A"


# -------
from typing import TypeGuard, Any
from typing import TypeAlias

Card: TypeAlias = tuple[str, str]
Deck: TypeAlias = list[Card]


def is_deck_of_cards(obj: Any) -> TypeGuard[Deck]:
    if not isinstance(obj, list):
        return False
    return all((isinstance(card_elem, str) for card_elem in card) for card in obj)


def get_score(card_or_deck: Card | Deck) -> int:
    if is_deck_of_cards(card_or_deck):
        pass


print(is_deck_of_cards("abc"))
print(is_deck_of_cards(("A", 'B')))
print(is_deck_of_cards((("A", 'B'), ('C', 'D'))))
c = Card(('A', 'B'))
d = Deck()
d.append(c)
print(is_deck_of_cards((("A", 'B'), ('C', 'D'))))
print(is_deck_of_cards(d))

l = []
t = ('A', 'B')
l.append(t)
print(is_deck_of_cards(l))

import inspect

inspect.get_annotations(is_deck_of_cards)
