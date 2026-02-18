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
            