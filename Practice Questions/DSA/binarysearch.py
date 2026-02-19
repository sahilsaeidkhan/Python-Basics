# 1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

# numbers = [1,4,6,9,10,5,7]


#because it is not sorted , first sort the array then perform binary search 

numbers = [1,4,5,6,7,9,10]

def find(target):
    start = 0
    end = len(numbers) - 1

    while(start<=end):
        mid = start + ( ( end - start ) //2)

        if target>numbers[mid]:
            start = mid+1
        elif target<numbers[mid]:
            end = mid-1
        else:
            print("It's present in the list")
            return mid
    
    print("It's not present in the list")



find(50)