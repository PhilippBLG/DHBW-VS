"""Unit tests for module scoop

Authors:
    Wolfgang Funk <funk@dhbw-vs.de>

"""
from bowl import Scoop
from bowl import Bowl
from bowl import ChocBowl
from bowl import Cream


def test_scoop():
    s = Scoop("Vanilla")
    assert s.flavour == "Vanilla"


def test_scoop_str():
    s = Scoop("Vanilla")
    assert str(s) == "Scoop with flavour 'Vanilla'"


def test_bowl():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    s3 = Scoop("Strawberry")
    b = Bowl(max_scoops=4, max_cream=1)
    b.add_scoops([s1])
    assert len(b._scoop_list) == 1
    b.add_scoops([s2, s3, Scoop("Raspberry")])
    assert len(b._scoop_list) == 4


def test_bowl_str():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    b = Bowl(max_scoops=4, max_cream=1)
    b.add_scoops([s1, s2])
    p = b.get_price()
    assert str(b) == f"Bowl for {p // 100} Euro and {p % 100} Cent contains:\n" \
                     "Scoop with flavour 'Vanilla'\n" \
                     "Scoop with flavour 'Chocolate'"


def test_bowl_price():
    b = Bowl(max_scoops=4, max_cream=1)
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    s3 = Scoop("Strawberry")
    b.add_scoops([s1, s2, s3])
    assert b.get_price() == Scoop.get_price() * 3


def test_bowl_limit():
    b = Bowl(max_scoops=4, max_cream=3)
    for _ in range(b._max_scoops):
        b.add_scoops([Scoop("Vanilla")])
    assert len(b._scoop_list) == b._max_scoops
    b.add_scoops([Scoop("Chocolate")])
    assert len(b._scoop_list) == 4
    for _ in range(b._max_cream):
        b.add_cream(Cream())
    assert len(b._cream_list) == 3


def test_choc_bowl_price():
    c = ChocBowl()
    assert c.get_price() == Scoop.get_price() * 3 + Cream.get_price()
    c.add_cream(Cream())
    assert c.get_price() == Scoop.get_price() * 3 + Cream.get_price() * 2
    c.add_scoops([Scoop("Chocolate")])
    assert c.get_price() == Scoop.get_price() * 4 + Cream.get_price() * 2


def test_choc_bowl_limit():
    c = ChocBowl()
    # Initial number of scoops is 3
    assert len(c._scoop_list) == 3
    # Only chocolate flavour
    for s in c._scoop_list:
        assert s.flavour == "Chocolate"
    # Only chocolate flavour can be added
    c.add_scoops([Scoop("Vanilla")])
    # Upper limit still applies
    assert len(c._scoop_list) == 3
    for _ in range(c._max_scoops - 3):
        c.add_scoops([Scoop("Chocolate")])
    assert len(c._scoop_list) == c._max_scoops
    c.add_scoops([Scoop("Chocolate")])
    assert len(c._scoop_list) == c._max_scoops


def test_choc_bowl_str():
    c = ChocBowl()
    c.add_cream(Cream(sugar=True))
    p = c.get_price()
    print(c)
    assert str(c) == f"Bowl for {p // 100} Euro and {p % 100} Cent contains:\n" \
                     "Pure cream serving\n" \
                     "Sugared cream serving\n" \
                     "Scoop with flavour 'Chocolate'\n" \
                     "Scoop with flavour 'Chocolate'\n" \
                     "Scoop with flavour 'Chocolate'"
