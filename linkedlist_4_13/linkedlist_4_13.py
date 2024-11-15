class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_node(head, x):
    new_node = Node(x)
    if head is None:
        return new_node

    prev = None
    current = head
    while current and current.value < x:
        prev = current
        current = current.next

    if prev:
        prev.next = new_node
        new_node.next = current
        return head
    else:
        new_node.next = head
        return new_node

def print_linked_list(head):
    if head is None:
        print("Empty")
        return
    current = head

    while current:
        print(current.value, end="")
        if current.next:
            print("->", end="")
        current = current.next
    print()

while True:
    try:
        n = int(input())
        queue = list(map(int, input().split("->")))
        x = int(input())

        head = None
        for num in queue:
            head = insert_node(head, num)

        position = 1
        current = head
        while current and current.value < x:
            position += 1
            current = current.next

        print(position)
        head = insert_node(head, x)
        print_linked_list(head)

    except EOFError:
        break