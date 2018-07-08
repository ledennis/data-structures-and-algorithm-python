# R-2.1
# 1. Fire Alarm
# 2. Pacemaker
# 3. Defibrillator

# R-2.2
# Whenever better hardware comes out, need to be able to port applications over with GUI updates to look fresh.
# If sofware is ran internationally, it must be flexible with different types of lawsselfself.

# R-2.3
# File tab of sublime. Methods are 'New Window', 'New File', 'Open ...', etc.

# R-2.4
class Flower:
    """ Flower class in R-2.4.

        name           name of Flower
        num_petals     number of petals
        price          price of Flower
    """

    def __init__(self, name, num_petals, price):
        """ Constructor for Flower. """
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self):
        """ Return name of Flower. """
        return self._name

    def set_name(self, name):
        """ Set name of Flower. """
        self._name = name

    def get_num_petals(self):
        """ Return num_petals of Flower. """
        return self._num_petals

    def set_num_petals(self, num_petals):
        """ Set num_petals for Flower. """
        self._num_petals = num_petals

    def get_price(self):
        """ Return price of Flower. """
        return self._price

    def set_price(self, price):
        """ Set price for Flower. """
        self._price = price

# R-2.5
class CreditCard:
    """ A consumer credit card. pg 70. """

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the acount identifier
        limit       credit limit
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """

        if isinstance(price, int) or isinstance(price, float):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        else:
            raise ValueError('Can only charge with money.')

    def make_payment(self, amount):
        """ Process customer payment that reducces balance. """

        # R-2.6
        if (amount < 0):
            raise ValueError('Negative payment not allowed.')
        self._balance -= amount


if __name__ == '__main__':
    # R-2.4
    redFlower = Flower('red', 12, 4)

    # Getters
    assert(redFlower.get_name() == 'red')
    assert(redFlower.get_num_petals() == 12)
    assert(redFlower.get_price() == 4)

    # Setters
    redFlower.set_name('blue')
    assert(redFlower.get_name() == 'blue')
    redFlower.set_num_petals(24)
    assert(redFlower.get_num_petals() == 24)
    redFlower.set_price(8)
    assert(redFlower.get_price() == 8)

    # R-2.5
    chase = CreditCard('Bob', 'Chase', '1234 5678 8765 4321', 4000)
    chase.charge(500.00)
    chase.charge(500)
    try:
        chase.charge('cookies')
        assert(False)
    except ValueError:
        assert(True)

    # R-2.6
    try:
        chase.make_payment(-789)
        assert(False)
    except ValueError:
        assert(True)
