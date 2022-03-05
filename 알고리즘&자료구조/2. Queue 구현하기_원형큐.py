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
        if (self.rear + 1) % MAX_QUEUE_SIZE == self.front:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isfull():
            print("Queue is full")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % MAX_QUEUE_SIZE

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % MAX_QUEUE_SIZE
            return value

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            peeked = self.queue[self.front + 1]
            return peeked