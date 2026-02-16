



city = input("Enter a city name ")

India = [ "mumbai" , "bangalore" , "pune" ,"delhi"]
Pakistan = [ "lahore" , "karachi" , "Islamabad"]

if city in India:
    print("The city belongs to India")
elif city in Pakistan:
    print("The city belongs to Pakistan")
else:
        print("The city belongs to Bangladesh")
















city1 = input("Enter 1st city name ")
city2 = input("Enter 2nd city name ")


if city1 in India and city2 in India or city1 in Pakistan and city2 in Pakistan:
    print("Both cities belong to same country")
else:
    print(" They don't belong to same Country")

























    sugar_level = input("Enter your sugar level")

    if sugar_level > 100 and sugar_level<120 :
         print("It's normal")
    elif sugar_level > 80 and sugar_level<100:
         print("It's low")
    elif sugar_level > 120:
         print("It's High")