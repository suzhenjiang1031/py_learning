class stack():
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

def Valid_Parenthesese(s):
    stack1 = stack()
    matching_brackets = {'(': ')', '[': ']', '<': '>', '{': '}'}
    for char in s:
        if char in matching_brackets.keys():
            stack1.push(char)
        elif char in matching_brackets.values():
            if stack1.is_empty() or matching_brackets[stack1.pop()] != char:
                return False
    return stack1.is_empty()


input_string = input("请输入需要测试的字符串：")
if Valid_Parenthesese(input_string):
    print("匹配成功！")
else:
    print("匹配失败！")