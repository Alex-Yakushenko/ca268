#!/usr/bin/evn python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def find(self, looking):
        while self != None:
            if self.data == looking:
                return self
            else:
                self = self.next
    def print_nodes(self):
        while self != None:
            print(self.data)
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
    return head
#assign()
def find_node():
    head = Node("Dublin")
    another_node = Node("Cork")
    head.next = another_node
    a_third_node = Node("Galway")
    another_node.next = a_third_node

    result = head.find("Galway")
    print(result.data)
#find_node()

def reverse(node):
    if node is None or node.next is None:
        return node
    new_head = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_head

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    new_head = Node(0)
    new_head.next = head
    
    prev_node = new_head
    
    while head and head.next:
        first_node = head
        second_node = head.next
        
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        
        prev_node = first_node
        head = first_node.next
        
    return new_head.next
def remove_nth_from_end(head, n):
    new_head = Node(0)
    new_head.next = head
    
    first = new_head
    second = new_head
    
    for _ in range(n+1):
        second = second.next
        
    while second:
        first = first.next
        second = second.next
        
    first.next = first.next.next
    
    return new_head.next

#ll = assign()
#ll = remove_nth_from_end(ll,7)
#ll = swap_pairs(ll)
#ll = reverse(ll)
#ll.print_nodes()


