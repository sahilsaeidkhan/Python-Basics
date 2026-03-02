class Mynumbers:
    def __init__(self):
        self.current = 0 

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1 

        if self.current>5:
            raise StopIteration
        
        return self.current
    
nums = Mynumbers()

for numbers in nums:
    print(numbers)

    