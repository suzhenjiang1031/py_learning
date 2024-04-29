while True:
    try:
        class Queue:
            def __init__(self, Max):
                self.MaxQueueSize = Max+1
                self.s = [None for x in range(self.MaxQueueSize)]
                self.front = 0
                self.rear = 0

            def EnQueue(self, x):
                if self.front != (self.rear+1) % self.MaxQueueSize:
                    self.rear += 1
                    self.s[self.rear] = x

            def DeQueue(self):
                self.front = self.front+1
                return self.s[self.front]

            def TraverseQueue(self):
                for i in range(self.front+1, self.rear+1):
                    print(self.s[i], end=' ')
                self.front, self.rear = 0, 0

            def isFull(self):
                if self.front == (self.rear+1) % self.MaxQueueSize:
                    return True

        n, m = map(int, input().split())
        Data = list(map(int, input().split()))
        ss = Queue(m)
        count = 1

        for i in Data:
            if i % 2 == 0:
                ss.EnQueue(i)
            if ss.isFull():
                print(str(count)+":", end='')
                ss.TraverseQueue()
                count += 1
                print()
            if len(Data)-Data.index(i)+1 < m:
                break

    except EOFError:
        break