with open("codebasics - tutorials/stocks.csv","r") as f , open("output.csv","w") as out:
    out.write("Company name , PE Ratio , PB Ratio\n")
    next(f)
    for line in f:
        token = line.split(',')
        stocks = token[0]
        price = float(token[1])
        eps = float(token[2])
        book = float(token[3])
        pe = round(price/eps,2)
        pb = round(price/book,2)

        out.write(f"{stocks} , {pe} , {pb} \n")












    with  open( "practice.txt" , "w") as info:
     info.write("Hi Everyone\nWe are learning File I/O")
     info.write("\nusing Python\nI like programming in Python")

    with open("practice.txt","r") as f:
      data = f.read()

    print(data.replace("Python" ,"Java"))













count = 0
with open("practice.txt","r") as f :
    data = f.read()
  
    nums = data.split(",")
    for val in nums:
      if (int(val) % 2==0):
        count+=1
print(count)

