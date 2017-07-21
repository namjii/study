
'''
1. 데이터를 큐에 Rear방향으로 저장(Enqueue)한다.
2. 데이터를 큐에서 Front방향으로 꺼내(Dequeue)낸다. 데이터를 Dequeue하고 나서는 큐에서 해당 데이터를 삭제된다.
3. 데이터를 큐에서 꺼내전에 잠깐 참조(Peek)할 수 있다.
4. 데이터가 비어 있다면(is_empty), Pop연산을 실행할 수 없다.
5. 데이터가 꽉차 있다면(is_full), Push연산을 실행할 수 없다. (단, 저장할 데이터의 개수를 한정해야함)
6. 큐에 있는 모든 데이터를 차례대로 출력할 수 있어야 한다.

'''


class CircularQueue(object):
    def __init__(self, max):
        self.queue = [None] * max  # max 길이의 리스트를 미리 만들어놓는다
        self.count = 0
        self.front = self.rear = 0
        self.max = max

    def enqueue(self, data):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.max
            self.queue[self.rear] = data
            self.count += 1

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.max
            self.count -= 1
            data = self.queue[self.front]
            self.queue[self.front] = None
            return data

    def peek(self):
        return self.queue[(self.front + 1) % self.max]

    def is_empty(self):
        return True if self.count == 0 else False

    def is_full(self):
        return True if self.count == self.max else False
# front 칸은 비어있어야함. 한칸을 비우지않으면 full일때랑 empty일때랑 가르키는게 똑같아서 구별못하기 때문임. 
# 그러면 is_full()도 로직이 바뀌어야함
    def display(self):
        print(self.queue)
