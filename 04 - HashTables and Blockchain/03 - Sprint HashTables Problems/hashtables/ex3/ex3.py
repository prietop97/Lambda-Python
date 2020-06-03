def intersection(arrays):

    my_hash = {}
    result = []

    # for i in range(len(arrays)):
    #     for j in range(len(arrays[i])):
    #         if arrays[i][j] in my_hash:
    #             my_hash[arrays[i][j]] += 1
    #         else:
    #             my_hash[arrays[i][j]] = 1

    
    # for key,value in my_hash.items():
    #     if value == len(arrays):
    #         result.append(key)

    for num in arrays[0]:
        my_hash[num] = True

    for i in range(1,len(arrays)):
        new_hash = {}
        for num in arrays[i]:
            if num in my_hash:
                new_hash[num] = True
        my_hash = new_hash

    return list(my_hash)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
