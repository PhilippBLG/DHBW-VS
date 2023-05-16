"""Unit tests for module bowl

Authors:
    Wolfgang Funk <funk@dhbw-vs.de>

"""
from bowl import Scoop
from bowl import Bowl


def test_scoop():
    s = Scoop("Vanilla")
    assert s.flavour == "Vanilla"


def test_scoop_str():
    s = Scoop("Vanilla")
    assert str(s) == "Scoop with flavour 'Vanilla'"


def test_bowl():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    b = Bowl()
    b.add_scoops([s1])
    assert len(b.scoop_list) == 1
    b.add_scoops([s2, Scoop("Raspberry")])
    assert len(b.scoop_list) == 3


def test_bowl_str():
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    b = Bowl()
    b.add_scoops([s1, s2])
    assert str(b) == "Bowl contains:\n" \
                     "Scoop with flavour 'Vanilla'\n" \
                     "Scoop with flavour 'Chocolate'"





