# Write a recursive function to calculate the sum of first n natural numbers.

def sum ( n):
    if n == 1:
        return 1
    n = n + sum(n-1)
    return n


print(sum (5))















# write a recursive function to print all elements in a list

books = ["Do Epic Shit,","The Metamorphosis,","The Almanack Of Naval Ravikant"]

def relist(index , books):
    if(index == len[books]):
        return print(books[index])
    
    print(books[index] ,  end = " ")
    relist(index+1,books)

print(relist(0,books))
