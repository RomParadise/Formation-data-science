import pytest
from module1.bank_account import BankAccount


def test_initial_balance():
    acc = BankAccount("Alice")
    assert acc.balance == 0.0
    assert acc.history == []


def test_deposit():
    acc = BankAccount("Alice")
    acc.deposit(100)
    assert acc.balance == 100
    assert acc.history[-1] == {"type": "deposit", "amount": 100, "balance_after": 100}


def test_withdraw():
    acc = BankAccount("Alice", balance=200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_deposit_negative_raises():
    acc = BankAccount("Alice")
    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_withdraw_insufficient_raises():
    acc = BankAccount("Alice", balance=10)
    with pytest.raises(ValueError):
        acc.withdraw(100)


def test_history_order():
    acc = BankAccount("Alice")
    acc.deposit(100)
    acc.deposit(50)
    acc.withdraw(30)
    assert len(acc.history) == 3
    assert acc.balance == 120