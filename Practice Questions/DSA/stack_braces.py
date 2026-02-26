class Braces:
    def __init__(self):
        self.list = []

    def push(self,value):
        return self.list.append(value)
    
    def pop(self):
        return self.list.pop()
    
    def isempty(self):
        return len(self.list) == 0 
    
class Check:
    def __init__(self,string):
        self.str = string

        self.pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

    def balance(self):
    
           b = Braces()
 
           for ch in self.str:
             if ch in "({[":
               b.push(ch)

             elif ch in ")}]":
                 if b.isempty():
                   print("false")

                 top = b.pop()

               

                 if top != self.pairs[ch] :
                  return False
            
            
             return b.isempty()


c = Check("(){i know( that) you are [speaking truth]}")
print(c.balance())