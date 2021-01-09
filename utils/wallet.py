from utils.exceptions import InsufficientAmount, NegativeAmount


class Wallet(object):
    """Wallet class

    Args:
        initial_amount (int): Sets the initial amount in the wallet
    """

    AMOUNT_ADDED = 0
    AMOUNT_SPENT = 0

    def __init__(self, initial_amount=0):
        if isinstance(initial_amount, int):
            if initial_amount < 0:
                raise NegativeAmount()
            self.amount = initial_amount
        else:
            raise TypeError("Amount should be of type int")

    def add_amount(self, amount):
        """Method to add amount in the wallet

        Args:
            amount (int): Add the amount
        """
        if isinstance(amount, int):
            if amount < 0:
                raise NegativeAmount()
            self.amount += amount
            self.AMOUNT_ADDED += amount
            return self._total_amount()
        else:
            raise TypeError("Amount should be of type int")

    def spend_amount(self, amount):
        """Method to spend money from total amount left

        Args:
            amount (int): Deducts amount from wallet
        """
        if isinstance(amount, int):
            if amount > self._total_amount():
                raise InsufficientAmount()
            self.amount -= amount
            self.AMOUNT_SPENT += amount

            return self._total_amount()
        else:
            raise TypeError("Amount should be of type int")

    def get_total_amount(self):
        return self._total_amount()

    def _total_amount(self):
        """Returns the total amount left"""
        return self.amount