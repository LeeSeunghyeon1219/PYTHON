MAX_STACK_SIZE = 3

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def isfull(self):
        if self.top >= MAX_STACK_SIZE - 1:
            return True
        else:
            return False

    def push(self, data):
        if self.isfull():
            print("Stak is Full")
        else:
            self.stack.append(data)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            value = self.stack.pop()
            self.top -= 1
            return value

    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]