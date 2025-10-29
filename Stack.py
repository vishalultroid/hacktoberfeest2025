from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return None
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            return None
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.top())   # 30
    print(stack.pop())   # 30
    print(stack.top())   # 20
    print(stack.empty()) # False
