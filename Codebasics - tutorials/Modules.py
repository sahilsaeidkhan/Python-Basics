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