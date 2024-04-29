class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_palindrome(s):
    stack = Stack()
    length = len(s)

    for i in range(length // 2):
        stack.push(s[i])

    if length % 2 == 0:
        start = length // 2
    else:
        start = length // 2 + 1

    for i in range(start, length):
        if s[i] != stack.pop():
            return False

    return True


input_str = input()

print(input_str)

if is_palindrome(input_str):
    print("Yes")
else:
    print("No")