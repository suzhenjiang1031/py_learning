class ArrayQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items[-1]