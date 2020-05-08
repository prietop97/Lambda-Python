def intersection(arrays):

    my_hash = {}
    result = []

    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if arrays[i][j] in my_hash:
                my_hash[arrays[i][j]] += 1
            else:
                my_hash[arrays[i][j]] = 1

    
    for key,value in my_hash.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
