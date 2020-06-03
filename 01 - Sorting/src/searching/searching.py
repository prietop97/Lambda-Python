# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr) - 1

  # TO-DO: add missing code
  while low <= high:
    middle_point = (high + low) // 2
    if arr[middle_point] == target:
      return middle_point
    elif arr[middle_point] > target:
      high = middle_point - 1
    elif arr[middle_point] < target:
      low = middle_point + 1
    else:
      break


  return -1 # not found

my_arr = [2,3,5,6,7,8,10]
#print(binary_search(my_arr,7))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] == target:
    return middle
  elif low > high:
    return - 1
  elif arr[middle] > target:
    return binary_search_recursive(arr,target,low,middle - 1)
  elif arr[middle] < target:
    return binary_search_recursive(arr,target,middle + 1,high)


print(binary_search_recursive(my_arr,10,0,len(my_arr)))