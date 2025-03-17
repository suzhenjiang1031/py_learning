class listNode:
    def __init__(self, id=0, name="", score=0):
        self.id = id
        self.name = name
        self.score = score
        self.next = None

def build_listNode():
    head = None
    tail = None
    while True:
        line = input().strip()
        if line == '#':
            break
        id, name, score = line.split()
        node = listNode(id, name, score)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def print_linedlistt(head):
    current = head
    while current:
        print(f"{current.id},{current.name},{current.score}",end = "")
        if current.next:
            print("->", end = "")
        current = current.next
    print()

while True:
    try:
        head = build_listNode()
        print_linedlistt(head)
    except EOFError:
        break