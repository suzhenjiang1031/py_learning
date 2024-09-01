class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

def remove_duplicates(head):
    if not head:
        return head

    current = head
    while current.next:
        if current.value == current.next.value:
            current.next == current.next.next
        else:
            current = current.next

    return head

def print_linked_list(head):
    if not head:
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
        values = list(map(int, input().split()))

        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        head = remove_duplicates(head)

        print_linked_list(head)

    except EOFError:
        break