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
    
    '''
    def sort(self, n):
        n = len(self.items)
        if n == 1:
            return self.items
        for i in range(n-1):
            if self.items[i] < self.items[i+1]:
                self.items[i], self.items[i+1] = self.items[i+1], self.items[i]

        sort(self.items, n - 1)
        return self.items
    '''
        
        

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

def bin_seq(number):
    queue = Queue()
    queue.enqueue("1")
    i = 0
    while i < number:
        binary = queue.dequeue()
        print(binary)
        queue.enqueue(binary + "0")
        queue.enqueue(binary + "1")
        i += 1
#bin_seq(16)

def lifo_seq(message):
    first_stack = Stack()
    output = []
    for i in message:
        if i == "*":
            output.append(first_stack.pop())
        else:
            first_stack.push(i)
    print(output)
#lifo_seq('EAS*Y*QUE***ST***IO*N***')

def fifo_seq(message):
    queue = Queue()
    output = []
    for i in message:
        if i == "*":
            output.append(queue.dequeue())
        else:
            queue.enqueue(i)
    print(output)
#fifo_seq('EAS*Y*QUE***ST***IO*N***')

def stack_reverse(message):
    stack = Stack()
    for i in message:
        stack.push(i)
    output = ""
    for i in range(stack.size()):
        output += stack.pop()
    print(output)
#stack_reverse("hello!")

def postfix(expression):
    stack = Stack()
    operators = "+-*/^"
    for i in expression:
        if i in operators:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.push({"+" : a + b, "-" : a - b, "*" : a * b, "/" : a / b, "^" : a ** b}[i])
        else:
            stack.push(i)
    print(stack.pop())
#postfix("1432^*+147--+")
