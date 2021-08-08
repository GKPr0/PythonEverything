from sys import  getsizeof
from SupportFunctions import timeit, HEADER, LINK
from dataclasses import dataclass, make_dataclass, field, fields
from typing import Any, List

LINK("https://realpython.com/python-data-classes/")

HEADER("Simple Data Class vs Regular Class")
@dataclass
class Card:
    rank: str
    suit: str


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


card = Card('Q', 'Hearts')
print(card)
print(card.rank)
print(card == Card('Q', 'Hearts'))

regular_card = RegularCard('Q', 'Hearts')
print(regular_card)
print(regular_card.rank)
print(regular_card == RegularCard('Q', 'Hearts'))


# ----------------------------------------------
HEADER("Alternative way of making Data Class")

Position = make_dataclass('Position', ['name', 'lat', 'lon'])

position = Position("Praha", 55, 24)
print(position)
print(position.name)


HEADER("Creating dataclass without specific type")

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

print(WithoutExplicitTypes("Ondra", "test"))
print(WithoutExplicitTypes("Test"))


# ----------------------------------------------
HEADER("More flexible Data Classes")


@dataclass
class Position:
    name: str = field(repr=False)
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


print(Position("Praha", 55, 24))
print(fields(Position)[2].metadata['unit'])

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts)


@dataclass
class Deck:
    # cards: List[PlayingCard] = make_french_deck() -> Will NOT work
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):  # Override basic data class __repr__
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


print(Deck())
print(Deck(sorted(make_french_deck())))


# ----------------------------------------------
HEADER("Immutable Data Classes")


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = Position('Oslo', 10.8, 59.9)
print(pos.name)
try:
    pos.name = "Praha"
except Exception as e:
    print(e)


# ----------------------------------------------
HEADER("Inheritance")


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


print(Capital('Oslo', 10.8, 59.9, 'Norway'))

