import unittest
from base_model import BankAccount, MaximalWithdrawException, OverdraftMaxException, NegativeDepositException

class BankAccountTest(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount("123456", "Blerta Sefaj", 500.0)
        account.deposit(100)
        self.assertEqual(account.balance, 600.0)

    def test_withdraw_sufficient_funds(self):
        account = BankAccount("123456", "Blerta Sefaj", 500.0)
        account.withdraw(300)
        self.assertEqual(account.balance, 200.0)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("123456", "Blerta Sefaj", 500.0)
        with self.assertRaises(OverdraftMaxException):
            account.withdraw(1000)

    def test_withdraw_exceed_maximal_withdraw(self):
        account = BankAccount("123456", "Blerta Sefaj", 500.0)
        with self.assertRaises(MaximalWithdrawException):
            account.withdraw(1500)

    def test_deposit_negative_amount(self):
        account = BankAccount("123456", "Blerta Sefaj", 500.0)
        with self.assertRaises(NegativeDepositException):
            account.deposit(-100)

if __name__ == '__main__':
    unittest.main()
