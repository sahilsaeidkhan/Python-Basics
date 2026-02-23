arr = [1,2,3,4,5,6]
target = 11


def exist(arr,target):
      
      start = 0
      end = len(arr) -1
      while start<end:

        sum = arr[start]+arr[end]

        if sum==target:
            return True
        elif sum<target:
          start+=1
        else:
           end-=1
    

      return False

print(exist(arr,target))