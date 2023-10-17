class Stack:
    """
    Python implementation the stack
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    def reverse(self):
        return self.items[::-1]
    def sort(self):
        n = len(self.items)
        if n == 1:
            return self.items
        for i in range(n-1):
            if self.items[i] < self.items[i+1]:
                self.items[i], self.items[i+1] = self.items[i+1], self.items[i]

        sort(self.items, n - 1)
        return self.items
        
        

class Queue:
    """
    Python implementation the queue
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    """
    Python implementation the deques
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_first(self, e):
        self.items.insert(0, e)

    def add_last(self, e):
        self.items.append(e)

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(4)
stack.push(3)
stack.push(5)