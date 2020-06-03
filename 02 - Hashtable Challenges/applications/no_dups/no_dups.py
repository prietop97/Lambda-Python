def no_dups(s):
    s_arr = s.split()
    my_hash = {}
    returning = []
    returning_s = ""
    for word in s_arr:
        if word not in my_hash:
            returning.append(word)
            my_hash[word] = True

    for i in range(len(returning)):
        if len(returning) - 1 == i:
            returning_s += returning[i]
        else:
            returning_s += returning[i] + " "

    return returning_s

    




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))