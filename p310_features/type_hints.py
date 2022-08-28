from typing import List, Union


def sum_list(numbers: List[Union[float, int]]) -> float:
    pass


def new_sum_list(numbers: list[float | int]) -> float | int:
    pass


user_id = 1234
isinstance(user_id, str | int)

# --------
from typing import TypeAlias

Card: TypeAlias = tuple[str, str]
Deck: TypeAlias = list[Card]


def get_ace(suit: str | None) -> tuple[str, str]:
    if suit is None:
        suit = 'K'

    return suit, "A"


# -------
from typing import TypeGuard, Any


def is_deck_of_cards(obj: Any) -> TypeGuard[Deck]:
    return isinstance(obj, Deck)


def get_score(card_or_deck: Card | Deck) -> int:
    if is_deck_of_cards(card_or_deck):
        pass


t = is_deck_of_cards("abc")


import inspect

inspect.get_annotations(is_deck_of_cards)