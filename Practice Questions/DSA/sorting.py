## bubble sort 

arr = [8,3,6,1,6]
n = len(arr)

for i in range(n):
    for j in range(n-1):

        if arr[j] > arr[j+1]:
            # swap 
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

    
print(arr)



























#bubble sort 

elements = [
{ 'name': 'mona','transaction_amount': 400,'device': 'iphone-10'},
{ 'name': 'dhaval', 'transaction_amount': 200,'device': 'google pixel'},
{ 'name': 'kathy', 'transaction_amount': 800,'device': 'vivo'},
{'name': 'aamir','transaction_amount': 1000, 'device': 'iphone-8'},
]

n = len(elements)

for i in range(3):
   key = input("Enter key to sort ( name , amount , device):")



if key == "name":
    sort_key = "name"
elif key == "amount":
    sort_key = "transaction_amount"
elif key == "device":
    sort_key = "device"

else:
    print("Invalid input")



for i in range(n):
    for j in range(n-i-1):
        if elements[j][sort_key] > elements[j+1][sort_key]:
#swap
                  elements[j] , elements[j+1] = elements[j+1],elements[j] 

print("\nSorted List")
for items in elements:
     print(items)