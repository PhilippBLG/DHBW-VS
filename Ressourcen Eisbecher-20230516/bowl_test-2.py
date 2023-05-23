"""Unit tests for module scoop

Authors:
    Wolfgang Funk <funk@dhbw-vs.de>

"""
from bowl import Scoop
from bowl import Bowl


def test_scoop():
    s = Scoop("Vanilla")
    assert s._flavour == "Vanilla"


def test_scoop_str():
    s = Scoop("Vanilla")
    assert str(s) == "Scoop with flavour 'Vanilla'"


def test_bowl():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    s3 = Scoop("Strawberry")
    b = Bowl()
    b.add_scoops([s1])
    assert len(b._scoop_list) == 1
    b.add_scoops([s2, s3, Scoop("Raspberry")])
    assert len(b._scoop_list) == 4


def test_bowl_str():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    b = Bowl()
    b.add_scoops([s1, s2])
    p = b.get_price()
    assert str(b) == f"Bowl for {p // 100} Euro and {p % 100} Cent contains:\n" \
                     "Scoop with flavour 'Vanilla'\n" \
                     "Scoop with flavour 'Chocolate'"


def test_bowl_price():
    b = Bowl()
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    s3 = Scoop("Strawberry")
    b.add_scoops([s1, s2, s3])
    assert b.get_price() == Scoop.price * 3


def test_bowl_limit():
    b = Bowl()
    for _ in range(Bowl.max_scoops):
        b.add_scoops([Scoop("Vanilla")])
    assert len(b._scoop_list) == Bowl.max_scoops
    b.add_scoops([Scoop("Chocolate")])
    assert len(b._scoop_list) == Bowl.max_scoops
