a = input("Enter a number :")
b = input("Enter a number :")
try:
      c = a/b
except Exception as e:
      print('Exception occured:' , e)
      c = None
print(c)


















a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

try:
    c = a/b
except ZeroDivisionError as e:
    print("Zero Division Error")
    c = "Infinite"

print(c)























try:
    marks = int(input("Enter your marks: "))
    
    if marks<0 or marks>100:
        raise ValueError("Enter in range of 1 to 100")

    if marks>=90 and marks<=100:
        print("A Grade")
    elif marks>=80 and marks<=89:
        print("B Grade")
    elif marks>=70 and marks<=79:
        print("C Grade")
    elif marks>=60 and marks<=69:
        print("D Grade")
    else:
        print("F")

except ValueError as e:
  print("Error:" , e)

finally:
    print("Thank you for using the Grade Calculator")
































































