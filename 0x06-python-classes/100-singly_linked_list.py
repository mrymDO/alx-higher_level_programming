#!/usr/bin/python3
""" Singly linked list"""


class Node:
    """ Class defines a node of singly linked list"""
    def __init__(self, data, next_node=None):
        """
        Initializes a Node object.
        Args:
            data: data to be stored in node
            next_node: reference to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get data value stored in the node """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter for data value of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """reference to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node reference"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class that defines a singly linked list"""
    def __init__(self):
        """Initializes an empty object"""
        self.__head = None

    def __str__(self):
        """returns string representation of the linked list"""
        temp2 = self.__head
        result = []
        while temp2 is not None:
            result.append(str(temp2.data))
            temp2 = temp2.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """ Inserts a new node in sorted order in the linked list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (
                temp.next_node is not None
                and temp.next_node.data < value
            ):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node
