with open("robin.txt") as f:
    words = f.read()
    exep = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    my_word = words
    for char in words:
        if char in exep:
            my_word = my_word.replace(char,"")
    splitted_words = my_word.split()
    my_hash = {}
    for word in splitted_words:
        if word in my_hash:
            my_hash[word] += 1
        else:
            my_hash[word] = 1
    
    items = list(my_hash.items())
    items.sort(reverse = True)
    items.sort(key = lambda x : x[1], reverse = True)
    for item in items:
        print(f'{item[0]} {"#" * item[1]}')