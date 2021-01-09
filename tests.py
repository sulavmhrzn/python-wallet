from utils.wallet import Wallet
from utils import exceptions
import unittest


class TestWallet(unittest.TestCase):
    def test_default_initial_amount(self):
        wallet = Wallet()
        self.assertEqual(wallet.amount, 0)

    def test_setting_initial_amount(self):
        wallet = Wallet(100)
        self.assertEqual(wallet.amount, 100)

    def test_setting_initial_amount_raises_type_error_exception(self):
        with self.assertRaises(TypeError):
            Wallet("1")

    def test_setting_initial_amount_raises_negativeamount_exception(self):
        with self.assertRaises(exceptions.NegativeAmount):
            Wallet(-2)

    def test_wallet_add_amount(self):
        wallet = Wallet(100)
        result = wallet.add_amount(100)
        self.assertEqual(result, 200)

    def test_wallet_add_amount_raises_type_error_exception(self):
        wallet = Wallet()
        with self.assertRaises(TypeError):
            wallet.add_amount("1")

    def test_wallet_add_amount_raises_negativeamount_exception(self):
        wallet = Wallet()
        with self.assertRaises(exceptions.NegativeAmount):
            wallet.add_amount(-100)

    def test_wallet_spend_amount(self):
        wallet = Wallet(100)
        result = wallet.spend_amount(50)
        self.assertEqual(result, 50)

    def test_wallet_spend_amount_raises_insufficientamount_exception(self):
        wallet = Wallet(100)
        with self.assertRaises(exceptions.InsufficientAmount):
            wallet.spend_amount(200)

    def test_wallet_spend_amount_raises_type_error_exception(self):
        wallet = Wallet(100)
        with self.assertRaises(TypeError):
            wallet.spend_amount("2")

    def test_wallet_total_amount(self):
        wallet = Wallet(100)
        self.assertEqual(wallet._total_amount(), 100)
        wallet.add_amount(200)
        self.assertEqual(wallet._total_amount(), 300)
        wallet.spend_amount(50)
        self.assertEqual(wallet._total_amount(), 250)


unittest.main()