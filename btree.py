class Node2(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Btree(object):
    def __init__(self, root):
        self.root = Node2(root)

    def insert(self, val):
        self.insert_help(self.root, val)

    def insert_help(self, current, val):
        if current.value < val:
            if current.right:
                self.insert_help(current.right, val)
            else:
                current.right = Node2(val)
            if current.left:
                self.insert_help(current.left, val)
            else:
                current.left = Node2(val)

    def search(self, find):
        self.search_help(self.root, find)

    def search_help(self, current, find):
        if current:
            if current.value == find:
                return True
            elif current.value < find:
                return self.search_help(current.right, find)
            else:
                return self.search_help(current.left, find)