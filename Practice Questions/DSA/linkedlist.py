class Bottle:
    def __init__(self,data):
        self.data = data
        self.next = "None"

c = Bottle(4)
print(c.data)