class stack:
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

def decimal_to_binary(n):
    if n == 0:
        return '0'

    stack1 = stack()

    while n > 0:
        remainder = n % 2
        stack1.push(remainder)
        n = n // 2

    binary_string = ''
    while not stack1.is_empty():
        binary_string += str(stack1.pop())
    return binary_string

input_string = int(input("请输入一个非负整数："))
result_string = decimal_to_binary(input_string)
print(f"{input_string}的二进制表示为{result_string}")

def decimal_to_octonary(n):
    if n == 0:
        return '0'

    stack2 = stack()

    while n > 0:
        octonary_number = n % 8
        stack2.push(octonary_number)
        n = n // 8

    octonary_string = ''

    while not stack2.is_empty():
        octonary_string += str(stack2.pop())
    return octonary_string

input_string = int(input("请输入你要转化成八进制的数字："))
result_string = decimal_to_octonary(input_string)
print(f"{input_string}转化为八进制为{result_string}")
