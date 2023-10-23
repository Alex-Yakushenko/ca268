#!/usr/bin/evn python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def find(self, looking):
        while self.next != None:
            if self.data == looking:
                return self
            else:
                self = self.next
'''
class Linked_list:
    def __init__(self, i):
        self.head = Node(i)
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = none
list_obj = Linked_list(2)
'''
def assign():
    head = Node(0)
    prev = head
    for i in range(2,101,2):
        current = Node(i)
        prev.next = current
        prev = current
    tmp = head
    while tmp.next != None:
        #print(tmp.data)
        tmp = tmp.next
#assign()
def find_node()
    head = Node("Dublin")
    another_node = Node("Galway")
    head.next = another_node
    a_third_node = Node("Cork")
    another_node.next = a_third_node

    result = head.find("Galway")
    print(result.data)
#find_node()

