class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def is_palindrome(s):
    stack1 = Stack()

    for char in s:
        stack1.push(char)

    for char in s:
        if char != stack1.pop():
            return False
        else:
            return True


input_string = input("输入需要测试的字符串：")
if is_palindrome(input_string):
    print(f"{input_string}是回文序列")
else:
    print(f"{input_string} 不是回文序列")
