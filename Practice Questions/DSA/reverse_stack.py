class Stack:
    def __init__(self):
        self.string = []

    def push(self,value):
         self.string.append(value)
    
    def pop(self):
        if not self.isempty() :
             return self.string.pop()
        return None

    def isempty(self):
        return len(self.string) == 0 
    
class ReverseString:
      def __init__(self,text):
           self.text = text

      def  reverse(self):
           s = Stack()
           for ch in self.text:
                s.push(ch)
         
           Reverse = ""
           while not s.isempty():   
             Reverse += s.pop()
           return Reverse

        
r1 = ReverseString("iah ihn ih raazetni ot bA - ihn ih laalam iok ot bA")
print(r1.reverse())