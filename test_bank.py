# Part 12 (Challenge) - Test the bank account
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# Run:  pytest test_bank.py -v     (then take a screenshot of all tests passing)

import pytest

from part09_oop import BankAccount


@pytest.fixture
def account() -> BankAccount:
    """A fresh account with Rs 1000 for every test."""
    return BankAccount("Ali", 1000)


def test_deposit_increases_balance(account: BankAccount) -> None:
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw_decreases_balance(account: BankAccount) -> None:
    account.withdraw(300)
    assert account.balance == 700


def test_history_records_every_transaction(account: BankAccount) -> None:
    account.deposit(200)
    account.withdraw(100)
    assert len(account.history) == 2
    assert "Deposit" in account.history[0]
    assert "Withdraw" in account.history[1]


def test_new_account_has_empty_history(account: BankAccount) -> None:
    assert account.history == []


def test_deposit_negative_amount_raises(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.deposit(-50)
    assert account.balance == 1000   # balance must not change


def test_withdraw_more_than_balance_raises(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.withdraw(5000)
    assert account.balance == 1000


def test_withdraw_negative_amount_raises(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.withdraw(-10)
