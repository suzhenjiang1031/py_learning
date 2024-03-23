class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
while True:
    try:
        N=int(input())
        S=list(map(int,input().split()))

        head=Node(None)
        cNode=head
        for i in range(N):
            newNode=Node(S[i])
            cNode.next=newNode
            cNode=cNode.next

        cNode=head
        while cNode!=None and cNode.next!=None:
            cNode=cNode.next
            if cNode!=None and cNode.next!=None:
                print(cNode.data,"->",sep="",end="")
        if cNode!=None:
            print(cNode.data)


    except EOFError:
        break