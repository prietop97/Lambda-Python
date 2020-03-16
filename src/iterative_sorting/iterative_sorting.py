import random

my_arr = [random.randint(0,5) for _ in range(6)]
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i,len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

#print(selection_sort([random.randint(0,22) for _ in range(30)]))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted_index = len(arr) - 1
    while sorted_index > 0:

        for i in range(sorted_index):

            if(arr[i] > arr[i + 1]):
                temp = arr[i + 1]
                arr[i+1] = arr[i]
                arr[i] = temp
            
        sorted_index -= 1



    return arr

#print(selection_sort([random.randint(0,22) for _ in range(30)]))




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ): #arr len = N  K
    ## An array of the length of the range of the incoming arr
    my_arr = [0] * (maximum + 1)

    ## Increment the value in my_arr at the index of the value of arr[i]
    ## It counts how many times the number occurs
    for i in range(len(arr)):
        my_arr[arr[i]] += 1


    
    #### RETURNING NEW ARR 
    ## SPACE COMPLEXITY OF (n + k) k = range    n = len of arr
    ## TIME COMPLEXITY OF (n + k) k = range   n = len of arr
    # Make a new array of length of the original arr
    # Decrement my_arr[i] by one
    # Look at the starting index of arr[i] in my_arr
    # change returning_arr at the index we got to the value of arr[i]

    ## Loop through my arr and add the value of the index before to the current index 
    ## How many elements come before the current element
    # for i in range(1,len(my_arr)):
    #     my_arr[i] += my_arr[i - 1]

    # returning_arr = [0] * len(arr)
    # for i in range(len(arr)):
    #     my_arr[arr[i]] -= 1
    #     index_of_current = my_arr[arr[i]]
    #     returning_arr[index_of_current] = arr[i]
        
    # for i in range(len(arr)):
    #     arr[i] = returning_arr[i]

    #### WITHOUT CREATING A NEW ARR 
    ## SPACE COMPLEXITY OF (k) k = range
    ## TIME COMPLEXITY OF ?? (k * ?) (k + n?)

    j = 0
    for k in range(len(my_arr)):
        for _ in range(my_arr[k]):
            arr[j] = k
            j += 1
            
    return arr


print(count_sort([random.randint(0,20) for _ in range(10)],20))


