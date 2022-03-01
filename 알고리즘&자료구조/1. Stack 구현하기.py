class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]