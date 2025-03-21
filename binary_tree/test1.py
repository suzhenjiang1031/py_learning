class ListNode:
    def __init__(self, student_id=0, name="", score=0, next=None):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.next = next

def build_linked_list():
    head = None
    tail = None
    while True:
        line = input().strip()
        if line == "#":
            break
        student_id, name, score = line.split()
        node = ListNode(student_id, name, score)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def find_student_info(head, target_id):
    current = head
    while current:
        if current.student_id == target_id:
            return current
        current = current.next
    return None

head = build_linked_list()

current = head
while current:
    print(f"{current.student_id},{current.name},{current.score}", end="")
    if current.next:
        print("->", end="")
    current = current.next
print()

target_id = input().strip()
student_info = find_student_info(head, target_id)
if student_info:
    print(f"{student_info.name},{student_info.score}")