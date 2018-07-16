import time
import random

class Router:
    """ Router class for that contains nodes.

        _network        dict that contains {name(str), Node}
        _orders         dict that contains {name(str), Packet}
    """
    def __init__(self):
        self._network = {}
        self._orders = []

    def add_node(self, Node):
        self._network[Node.get_name()] = Node

    def add_order(self, receiver, Packet):
        order = (receiver, Packet)
        self._orders.append(order)

    def complete_orders(self):
        completed = []
        if self._orders:
            for order in self._orders:
                if order[0] in self._network:
                    self.send_order(self._network[order[0]], order[1])
                    completed.append(order)
                else:
                    raise AttributeError(receiver + ' not in network.')

            for order in completed:
                self._orders.remove(order)

    def send_order(self, node, Packet):
        node.receive_packets(Packet)

    def check_node(self, name):
        return name in self._network

class Node:
    def __init__(self, name, Router=None):
        self._name = name
        self._packets = []
        self._Router = Router

    def connect_to_router(self, Router):
        self._Router = Router
        self._Router.add_node(self)

    def send_packets(self, receiver, Packet):
        if self._Router is not None:
            if self._Router.check_node(receiver):
                self._Router.add_order(receiver, Packet)
            else:
                raise ValueError(receiver + ' is not in network.')
        else:
            raise AttributeError('Not connected to router.')

    def send_packets_periodically(self, receiver, Packet, timer=1, loop=3):
        for i in range(loop):
            self.send_packets(receiver, Packet)
            time.sleep(timer)

    def receive_packets(self, Packet):
        self._packets.append(Packet)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_packets(self):
        return self._packets

    def check_packets(self):
        for packet in self._packets:
            print(packet.get_sender() + ' sent ' + str(packet.get_data()))

        del self._packets[:]

class Packet:
    def __init__(self, data, sender):
        self._data = data
        self._sender = sender

    def get_data(self):
        return self._data

    def get_sender(self):
        return self._sender

if __name__ == '__main__':
    router = Router()
    alice = Node('Alice', router)
    bob = Node('Bob')
    bob.connect_to_router(router)
    alice.send_packets_periodically('Bob', Packet(4, alice.get_name()))
    router.complete_orders()
    bob.check_packets()
