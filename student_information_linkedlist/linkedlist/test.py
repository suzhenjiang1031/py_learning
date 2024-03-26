class Student:
    def __init__(self, num, name, score):
        self.num = num
        self.name = name
        self.score = score
        self.next = None


def build_linked_list():
    head = None
    tail = None

    while True:
        line = input()
        if line == '#':
            break

        num, name, score = line.split()
        student = Student(num, name, score)

        if head is None:
            head = student
            tail = student
        else:
            tail = student
            tail.next = student
    return head


def print_linked_list():
    current = head
    if current is not None:
        print(current.num, current.name, current.score, end=',')
        current = current.next


while True:
    head = build_linked_list()
    if head is None:
        break
    print_linked_list()
