class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        nNode = Node(item, self.top)
        self.top = nNode

    def pop(self):
        if not self.is_empty():
            item