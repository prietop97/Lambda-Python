import random
from heap import Heap,HeapNode

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    splitted_words = words.split()
    my_hash = {}
    for i in range(len(splitted_words) - 1):
        word = splitted_words[i]
        if word == splitted_words[i + 1]:
            continue
        if word in my_hash:
            changed = False
            for node in my_hash[word].storage:
                if node.word == word:
                    node.value += 1
                    changed = True
            if not changed:
                node = HeapNode(splitted_words[i+1])
                my_hash[word].insert(node)
        else:
            heap = Heap()
            node = HeapNode(splitted_words[i+1])
            heap.insert(node)
            my_hash[word] = heap
    
    my_hash[splitted_words[len(splitted_words) - 1]] = None
    
    randomm = int(round(random.random() * len(my_hash)))
    keys = list(my_hash)
    sentance = ""
    last_word = keys[randomm]
    chaining = False


    while not chaining:
        if last_word[0].isupper():
            sentance += last_word
            break
        elif last_word[0] == "\"" and last_word[1].isupper():
            sentance += last_word
            break
        else:
            len_of_word = len(my_hash[last_word].storage)
            last_word = keys[int(round(random.random() * len(my_hash)))]
    
    ending = ['.','?','!']
    ending2 = ['."','?"','!"']

    end = True
    while end:
        if my_hash[last_word] == None:
            break
        sentance += " "
        temp = my_hash[last_word].storage[0].word
        sentance += my_hash[last_word].storage[0].word
        my_hash[last_word].storage[0].value -= 1
        if my_hash[last_word].storage[0].value <= 0:
            my_hash[last_word].storage.pop(0)
        
        my_hash[last_word]._sift_down(0)
        last_word = temp
        for x in ending:
            if last_word[-1] == x:
                end = False
        for y in ending2:
            if len(last_word) > 2:
                if last_word[-2] == y[0] and last_word[-1] == y[1]:
                    end = False
        
       
    
    
    print(sentance)



    
    

# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences
