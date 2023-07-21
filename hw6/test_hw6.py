from card import Card
from hand import Hand
from deck import Deck


def test_card_value():
    assert Card(Card.CLUBS, "2").value == 2
    assert Card(Card.CLUBS, "4").value == 4
    assert Card(Card.HEARTS, "10").value == 10
    assert Card(Card.HEARTS, "K").value == 10
    assert Card(Card.HEARTS, "Q").value == 10
    assert Card(Card.HEARTS, "J").value == 10
    assert Card(Card.HEARTS, "A").value == 11


def test_card_color():
    assert Card(Card.CLUBS, "2").color == "black"
    assert Card(Card.SPADES, "2").color == "black"
    assert Card(Card.HEARTS, "2").color == "red"
    assert Card(Card.DIAMONDS, "K").color == "red"


def test_card_display():
    assert Card(Card.CLUBS, "2").display == "2♣"
    assert Card(Card.SPADES, "10").display == "10♠"
    assert Card(Card.HEARTS, "K").display == "K♥"
    assert Card(Card.DIAMONDS, "A").display == "A♦"


def test_hand_add_one():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    assert h.total == 2


def test_hand_add_several():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    h.add(Card(Card.CLUBS, "A"))
    assert h.total == 13
    h.add(Card(Card.CLUBS, "K"))
    assert h.total == 23


def test_hand_reset():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    h.add(Card(Card.CLUBS, "A"))
    assert h.total == 13
    h.reset()
    assert h.total == 0
    h.add(Card(Card.CLUBS, "K"))
    assert h.total == 10
    h.reset()
    assert h.total == 0


def test_deck_size():
    d = Deck()
    assert d.size == 52
    d.deal()
    assert d.size == 51
    d.deal()
    assert d.size == 50

    d2 = Deck()
    assert d2.size == 52
    d2.deal()
    assert d2.size == 51


def test_deck_is_shuffled():
    d = Deck()
    cards_one = d.deal().display, d.deal().display, d.deal().display

    d2 = Deck()
    cards_two = d2.deal().display, d2.deal().display, d2.deal().display

    # shouldn't have drawn the same cards, indicates lack of shuffling
    assert cards_one != cards_two


def test_deck_reshuffle():
    d = Deck()
    first = d.deal()
    d.shuffle()
    # ensure the card wasn't placed back on top
    assert d.deal() != first
    while d.size > 1:
        d.deal()
    last = d.deal()
    assert first.display == last.display
