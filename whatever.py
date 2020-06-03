def weights(arr,length,limit):
    my_hash = {}
    for i in range(len(arr)):
        if arr[i] in my_hash:
            return [i,my_hash[arr[i]]]
        else:
            my_hash[limit - arr[i]] = i

print(weights([ 4, 6, 10, 18, 16 ],5,21))