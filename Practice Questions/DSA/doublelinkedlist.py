class Node:

    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c 
c.next = None 

a.prev = None
b.prev = a
c.prev = b 

class Linkedlist:

    def __init__(self):
        self.head = a
        self.tail = c        
    
    def print_forward(self):
        current = self.head
        while current:
            print(current.data,end = " ")
            current = current.next 

    def print_backward(self):
        current = self.tail
        print("\n")
        while current:
            print(current.data,end = " ")
            current = current.prev




ll = Linkedlist()
ll.print_forward()
ll.print_backward()

