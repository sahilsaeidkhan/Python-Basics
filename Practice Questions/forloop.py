result = ["heads", "tails","tails","heads", "tails", "heads","heads","tails","tails", "tails"]

count = 0 


for i in result:
    if i=="heads":
        count = count+1


#print(f"Heads came {count} times")

























for i in range(11):
    if i%2==0:
        continue
    else:
        b = i**2
       # print(b)























expense = [ 3423,2345,6786,8764]

#check = int(input("Enter expense"))
for i in expense:
    if check == 3423:
        print("Expense of January")
        break
    elif check == 2345:
        print("Expense of February")
        break
    elif check == 6786:
        print("Expense of March")
        break
    elif check == 8764:
        print("Expense of April")
        break
    else:
        print("Not in this expense list")

















finished = True


for i in range(5):
    check = input("Are you tired ")
    if check == "yes":
        print("You didn't finish the race")
        finished = False
        break
    


if finished == True:
   print("Successfully Completed the race")






















for i in range(1,11):
    print(i*i)










for i in range(6):
    for j in range(i):
        print("*", end="")
    
    print()