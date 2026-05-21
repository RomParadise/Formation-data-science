from module1.clean_script import mean_ignore_none, filter_above

def test_mean():
    assert mean_ignore_none([1, 2, 3]) == 2.0


def test_mean_ignore_none():
    assert mean_ignore_none([1, None , 3]) == 2.0
    

def test_filter_above():
    assert filter_above([1, 2, 3, 4, 5], 3) == [4, 5]


def test_filter_above_with_none():
    assert filter_above([1, None, 3, None, 5], 3) == [5]