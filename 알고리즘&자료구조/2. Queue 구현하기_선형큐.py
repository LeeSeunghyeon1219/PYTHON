MAX_QUEUE_SIZE = 3

class Queue:
    def __init__(self):
        self.queue = [None] * MAX_QUEUE_SIZE
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isfull(self):
        if self.rear >= MAX_QUEUE_SIZE - 1:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isfull():
            print("Queue is full")
        else:
            self.queue[self.rear] = data
            self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return value

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            peeked = self.queue[self.front]
            return peeked