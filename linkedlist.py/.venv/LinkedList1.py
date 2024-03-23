class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = '->' if current.next else "")
            current = current.next
        print()

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

while True:
    try:
        nums = list(map(int,input().split()))
        nums.pop()
        linked_list = LinkedList()
        for num in nums:
            linked_list.append(num)

        length = linked_list.length()
        print(length)
        linked_list.display()

    except EOFError:
        break