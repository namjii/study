'''
1. 데이터를 스택에 저장(Push)한다.
2. 데이터를 스택에서 꺼내(Pop)낸다. 데이터를 Pop하고 나서는 스택에서 해당 데이터를 삭제된다.
3. 데이터를 스택에서 꺼내전에 잠깐 참조(Peek)할 수 있다.
4. 데이터가 비어 있다면(is_empty), Pop연산을 실행할 수 없다.
5. 데이터가 꽉차 있다면(is_full), Push연산을 실행할 수 없다. (단, 저장할 데이터의 개수를 한정해야함)
6. 스택에 있는 모든 데이터를 차례대로 출력할 수 있어야 한다.

'''


class ArrayStack(object):
    def __init__(self, max):
        self.stack = []
        self.max = max
        self.count = 0

    def push(self, data):
        if not self.is_full():
            self.stack += [data]
            self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.stack[self.count - 1]
            del self.stack[self.count - 1]
            self.count -= 1
            return data

    def peek(self):
        return self.stack[self.count - 1]

    def is_empty(self):
        return True if self.count <= 0 else False

    def is_full(self):
        return True if self.count == self.max else False

    def display(self):
        print(self.stack)
