countries =  {"China": 143 , "India": 120 , "USA": 43, "Pakistan": 14}

for i in range(4):
  ask = input("Enter your input").lower()
  if ask == "print":
    for country, population in countries.items():
       print(f"{country}==>{population}")

  elif( ask == "add"):
    ask2 = input("Enter Country name to add")
    if ask2 in countries:
      print("Country Already exist")
    else:
      ask3 = int(input("Enter Population for the country"))
      countries[ask2] = ask3

  elif ( ask == "remove"):
    ask4 = input("Enter Country name to remove")
    if ask4 in countries:
      del countries[ask4]
      print(countries)
    else:
      print("Countries doesn't exist")

  elif ask == "query":
    query = input("query for which country")
    if query in countries:
     print(countries["query"])
    else:
      print("Country doesn't exist")



















prices = { "info" : [600,630,620]  , "ril" : [1430 , 1490 , 1397]  ,  "mtl" : [234,180,70] }

operation = input("Enter any operation( print or add):").lower()

if operation == "print":
    for stock,price in prices.items():
        avg = sum(price) / len(price)
        print(f"{stock} ==> {price} ==> {avg:.2f}")


elif operation == "add":
    stock_name = input("Enter name of the stock-")
    price = int(input("Enter price of the stock-"))

    if stock_name in prices:
        prices[stock_name].append(price)
    else:
        prices[stock_name] = [price]

print(prices)

























def circle_calc(r):

  print(f"Diameter is {r*2}")
  print(f"Circumference is {2*3.14*r*r}")
  print(f"Area is {3.14*r*r}")

r = int(input("Enter Radius:"))
circle_calc(r)


























from dictionary import circle_calc


circle_calc(5)




