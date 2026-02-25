class Stacks:
    def __init__(self):
        self.container = []

    def push(self,value):
        self.container.append(value)

    def pop(self):
       return self.container.pop()
        

    def peek(self):
        if self.container.isempty():
            return "Empty"
        else:
            return -1
        
    def isempty(self):
        return len(self.container) == 0 
        
    def size(self):
        return len(self.container)
    
s1 = Stacks()
s1.push(4)
s1.push(42)
s1.push(44)
s1.push(40)
print(s1.pop())
print(s1.container)

print(s1.isempty())

