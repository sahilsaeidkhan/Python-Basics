class Student:
     name = "Utkarsh"
     def __init__(self):
          print("Check hello")

S1 = Student()






















class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def avg(self):
        sum = 0
        for n in self.marks:
            sum+=n
        print("Percentile  of" , self.name ,"is" ,sum/3)



s1 = Student("Krishna",[94,94,98])
s1.avg()





















# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.


class Account:

    def __init__(self, balance , accountno):
        self.balance = balance
        self.account = accountno

    def debit(self,amount):
        self.balance-=amount
        print("Amount debited is" , amount)
        print("The remaining amount is", self.balance)
        
    def credit(self,amount):
        self.balance+=amount
        print("Amount credited is" ,amount)
        print("The remaining amount is", self.balance)



acc1 = Account(4500 ,58898212000335 )
acc1.debit(99)  
acc1.credit(24000)
  























# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:

    def __init__(self,radius):
        self.r = radius
    
    def Area(self):
        area = 3.14 * self.r * self.r
        print(area)

    def Perimeter(self):
        perimeter = round(2 * 3.14 * self.r,2) 
        print(perimeter)

c1 = Circle(5)
c1.Area()
c1.Perimeter()

