from module1.word_count import word_count


def test_empty_string():
    assert word_count("") == {}


def test_simple():
    assert word_count("hello world hello") == {"hello": 2, "world": 1}


def test_case_insensitive():
    assert word_count("Bonjour bonjour BONJOUR") == {"bonjour": 3}


def test_punctuation():
    result = word_count("Hello, world! Hello.")
    assert result == {"hello": 2, "world": 1}


def test_sorted_descending():
    result = word_count("a b b c c c")
    assert list(result.keys()) == ["c", "b", "a"]