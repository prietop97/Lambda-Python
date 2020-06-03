#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) Because even though we are looping while a is less than o(n^3) we are incrementing the a by n ^ 2 in each iteration


b) O(n logn) Because we are looping through n, and inside that loop we are looping once again but multiplying by 2 each time, making the second loop way faster

c) O(n) Because we are doing recursion once from n to 1 

## Exercise II

I would use binary search to search for the floor.

low - 0
high - len(n) - 1

while low < high
    half = high + low // 2
    throw egg
    if egg breaks
        throw egg at half - 1
        if egg breaks
            high = half - 1
        else
            return half
    elif egg doesnt break
        throw egg at half + 1
        if egg doesnt break
            low = half + 1
        else
            return half

time complexity = o(log(n))
    




