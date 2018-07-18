from random import randrange, randint

class River:
    """
        River class that handles turns of creatures

        length      length of river
    """
    def __init__(self, length=10):
        self._river = [None] * length

    def turns(self, loop=1):
        for i in range(1, loop+1):
            print('Turn ' + str(i))
            self.turn()

    def turn(self):
        """ One turn will happen on a river. """
        for index in range(len(self._river)):
            creature = self._river[index]
            if isinstance(creature, Creature):
                if self.fifty_fifty():
                    newPos = creature.move(len(self._river))
                    self.place(creature, newPos)
        self.print_river()

    def place(self, creature, pos):
        """ Places a creature on the river, cases are as follows:
            1) Pos is empty, move creature there or place if creature has not been placed.
            2) Pos is not empty, either populate if same species, or fish dies.
        """
        other_creature = self._river[pos]
        if other_creature is None:
            if creature.get_pos() is not None:
                self.put(creature, pos)
            else:
                creature.set_pos(pos)
                self._river[pos] = creature
        elif type(creature) is type(other_creature):
            if self.is_opposite_gender(creature, other_creature):
                self.populate(creature, other_creature)
            else:
                if self.is_stronger(creature, other_creature):
                    self.take_over(creature, pos)
                else:
                    self.decease_to_exist(creature)
        else:
            if isinstance(creature, Bear):
                self.take_over(creature, pos)
            else:
                self.decease_to_exist(creature)

    def decease_to_exist(self, creature):
        self._river[creature.get_pos()] = None

    def is_stronger(self, engager, defender):
        # Sneak attack rule: If same str, engager wins
        return engager.get_power() >= defender.get_power()

    def put(self, creature, pos):
        self._river[pos] = creature
        creature.set_pos(pos)

    def take_over(self, creature, pos):
        self._river[pos], self._river[creature.get_pos()] = creature, None
        creature.set_pos(pos)

    def populate(self, creature):
        """ Places Creature of type creature on random empty place if it exists. """
        newPos = self.find_rand_empty_place()
        if newPos > -1:
            newCreature = None
            if isinstance(creature, Bear):
                newCreature = Bear(gender=self.fifty_fifty(), power=randrange(0,9999))
            else:
                newCreature = Fish(gender=self.fifty_fifty(), power=randrange(0,9999))
            self.place(newCreature, newPos)

    def is_opposite_gender(self, mate, other_mate):
        return mate.get_gender() != other_mate.get_gender()

    def find_rand_empty_place(self):
        """ Returns list of empty places, returns -1 if not found. """
        list_none = [i for i, x in enumerate(self._river) if x == None]
        if list_none:
            return list_none[randint(0, len(list_none)-1)]
        else:
            return -1

    def fifty_fifty(self):
        """ Returns %50 chance of moving. """
        return randint(0,1) == 1

    def print_river(self):
        """ Prints current state of river. """
        for i in range(len(self._river)):
            if self._river[i]:
                print(str(i) + ' ' + self._river[i].type())
            else:
                print(str(i) + ' ' + 'None')
        print('\n')

class Creature:
    def __init__(self, gender=0, power=0, pos=None):
        self._power = power
        self._pos = pos

        if gender > 1:
            self._gender = 'M'
        else:
            self._gender = 'F'

    def get_power(self):
        return self._power

    def get_gender(self):
        return self._gender

    def get_pos(self):
        return self._pos

    def set_pos(self, pos):
        self._pos = pos

    def move(self, length):
        newPos = None
        if (self._pos == 0):
            newPos = self._pos+1
        elif (self._pos == length-1):
            newPos = self._pos-1;
        else:
            newPos = self._pos + randrange(-1,2,2)    # either 1 or -1
        return newPos

class Bear(Creature):
    def __init__(self, gender=0, power=0, pos=None):
        super().__init__(gender=gender, power=power, pos=pos)

    def type(self):
        return 'Bear'

class Fish(Creature):
    def __init__(self, gender=0, power=0, pos=None):
        super().__init__(gender=gender, power=power, pos=pos)

    def type(self):
        return 'Fish'

if __name__ == '__main__':
    river = River()
    bear1 = Bear(gender=1, power=2)
    bear2 = Bear(gender=0, power=3)
    fish1 = Fish(gender=1, power=4)
    fish2 = Fish(gender=0, power=5)
    river.place(bear1, 0)
    river.place(bear2, 1)
    river.place(fish1, 9)
    river.place(fish2, 8)
    river.turns(10)
