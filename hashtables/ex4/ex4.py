def has_negatives(a):
    my_hash = {}
    result = []
    for num in a:
        if num in my_hash:
            result.append(abs(num))
        else:
            my_hash[num * -1] = True
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
