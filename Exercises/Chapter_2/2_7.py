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


if __name__ == '__main__':
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
