class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self,value):
        self.list.append(value)

    def dequeue(self):
        if self.isempty():
            return None
        else:
             return self.list.pop(0)

    def isempty(self):
        return len(self.list) == 0
    
    def length(self):
        return len(self.list)
        





s = Queue()

s.enqueue(5)
s.enqueue(1)
s.enqueue("krishna")
print(s.dequeue())

