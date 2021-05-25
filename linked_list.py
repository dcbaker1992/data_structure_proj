from node import Node


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            temp = self.head
            node.next = temp
            self.head = node
            self.tail.next = self.head