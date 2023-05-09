import duplicate_check

def test_has_duplicate_version_one():
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5]) == False
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5, 1]) == True
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5, 1, 2]) == True
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5, 1, 2, 3]) == True
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5, 1, 2, 3, 4]) == True
    assert duplicate_check.has_duplicate_version_one([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == True