import intersect

def test_intersect():
    assert intersect.intersect([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert intersect.intersect([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 1]) == [1, 2, 3, 4, 5]
    assert intersect.intersect([1, 2, 3], [1, 2, 3, 4, 5, 1]) == [1, 2, 3]
