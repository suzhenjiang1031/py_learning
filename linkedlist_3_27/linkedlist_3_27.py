# 这是一个编程题模板。
#
# 根据输入的学生信息，建立学生信息单链表并查找某位学生成绩。
#
# 输入格式:
# 有n+2行：
#
# 前n行表示n个学生信息，每一行有3个数据项：学号，姓名和成绩，用空格分隔；
#
# 第n+1行为#，表示学生信息输入结束；
#
# 最后行是学号，根据该学号输出相应学生姓名和成绩。
#
# 输出格式:
# 第一行输出单链表，注意结尾的换行；
#
# 第二行输出学生姓名和成绩。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 1001 lilin 98
# 1002 niqing 87
# 1003 xiaoming 96
# #
# 1003
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 1001,lilin,98->1002,niqing,87->1003,xiaoming,96
# xiaoming,96

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

# 输入学生信息
head = build_linked_list()

# 输出单链表
current = head
while current:
    print(f"{current.student_id},{current.name},{current.score}", end="")
    if current.next:
        print("->", end="")
    current = current.next
print()

# 根据学号查找学生信息
target_id = input().strip()
student_info = find_student_info(head, target_id)
if student_info:
    print(f"{student_info.name},{student_info.score}")