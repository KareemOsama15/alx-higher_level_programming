#!/usr/bin/python3
"""Node module
"""


class Node:
    """Class Node that defines a node object
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList Module
"""


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a new node object
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        current = self.__head
        newElement = Node(value)
        if self.__head is None or value <= self.__head.data:
            newElement.next_node = self.__head
            self.__head = newElement
        else:
            while (current.next_node is not None and
                    value > current.next_node.data):
                current = current.next_node
            newElement.next_node = current.next_node
            current.next_node = newElement

    def __str__(self):
        current = self.__head
        val = ''
        while current is not None:
            val += str(current.data)
            if current.next_node is not None:
                val += '\n'
            current = current.next_node
        return (val)
