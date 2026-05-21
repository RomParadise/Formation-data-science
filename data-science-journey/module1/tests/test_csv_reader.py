import pytest
from module1.csv_reader import column_mean

CSV = "module1/data/sales.csv"


def test_mean_price():
    assert column_mean(CSV, "price") == pytest.approx(889.10, rel=1e-3)


def test_mean_quantity():
    assert column_mean(CSV, "quantity") == pytest.approx(1.8, rel=1e-3)


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        column_mean("nope.csv", "price")


def test_missing_column():
    with pytest.raises(KeyError):
        column_mean(CSV, "nonexistent")


def test_non_numeric_column():
    with pytest.raises(ValueError):
        column_mean(CSV, "product")