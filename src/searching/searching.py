# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(arr):
    if arr[i] == target:
      return arr[i]

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)
  middle_point = (high - low) // 2

  # TO-DO: add missing code
  while middle_point > high or middle_point < low:
    if arr[middle_point] == target:
      return middle_point
    elif arr[middle_point] > target:
      high = middle_point - 1
    else:
      low = middle_point + 1
    middle_point = (high - low) // 2

  return -1 # not found

my_arr = [2,3,5,6,7,8]
print(binary_search(my_arr,7))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
