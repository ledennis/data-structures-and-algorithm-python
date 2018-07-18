from random import *

class River:
    """
        River class that handles turns of creatures

        lenght      length of river
    """
    def __init__(self, length=10):
        self._river = [None] * length

    def turns(self, loop=1):
        for i in range(1, loop+1):
            print('Turn ' + str(i))
            self.turn()

    def turn(self):
        """ Randomly determines if creatures in list  move. """
        for index in range(len(self._river)):
            creature = self._river[index]
            if isinstance(creature, Creature):
                if self.should_move():
                    newPos = creature.move(len(self._river))
                    self.place(creature, newPos)
        self.print_river()

    def place(self, creature, pos):
        """ Places a creature on the river, cases are as follows:
            1) Pos is empty, move creature there or place if creature has not been placed.
            2) Pos is not empty, either populate if same species, or fish dies.
        """
        current_creature = self._river[pos]
        if current_creature is None:
            if creature.get_pos() is not None:
                self.take_over(creature, pos)
            else:
                creature.set_pos(pos)
                self._river[pos] = creature
        elif type(creature) is type(current_creature):
            self.populate(creature)
        else:
            if isinstance(creature, Bear):
                self.take_over(creature, pos)
            else:
                self._river[creature.get_pos()] = None

    def take_over(self, creature, pos):
        old_pos = creature.get_pos()
        self._river[pos] = self._river[creature.get_pos()]
        self._river[old_pos] = None
        creature.set_pos(pos)

    def populate(self, creature):
        """ Places Creature of type creature on random empty place if it exists. """
        newPos = self.find_rand_empty_place()
        if newPos > -1:
            newCreature = None
            if isinstance(creature, Bear):
                newCreature = Bear()
            else:
                newCreature = Fish()
            self.place(newCreature, newPos)

    def find_rand_empty_place(self):
        """ Returns list of empty places, returns -1 if not found. """
        list_none = [i for i, x in enumerate(self._river) if x == None]
        if list_none:
            return list_none[randint(0, len(list_none)-1)]
        else:
            return -1

    def should_move(self):
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
    def __init__(self, pos=None):
        self._pos = pos

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
    def __init__(self, pos=None):
        super().__init__(pos)

    def type(self):
        return 'Bear'

class Fish(Creature):
    def __init__(self, pos=None):
        super().__init__(pos)

    def type(self):
        return 'Fish'

if __name__ == '__main__':
    river = River()
    bear1 = Bear()
    bear2 = Bear()
    fish1 = Fish()
    fish2 = Fish()
    river.place(bear1, 0)
    river.place(bear2, 1)
    river.place(fish1, 9)
    river.place(fish2, 8)
    river.turns(10)
