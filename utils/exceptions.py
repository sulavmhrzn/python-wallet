class InsufficientAmount(Exception):
    """Raised when trying to spend the amount that is greater than the amount in the wallet."""

    def __init__(self, message="You have don't have sufficient amount to spend."):
        self.message = message
        super().__init__(self.message)


class NegativeAmount(Exception):
    """Raised when the amount is negative."""

    def __init__(self, message="Amount should not be a negative value"):
        self.message = message
        super().__init__(self.message)