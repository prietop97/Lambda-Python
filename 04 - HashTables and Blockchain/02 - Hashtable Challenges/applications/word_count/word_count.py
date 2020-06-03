def word_count(s):
    my_word = s
    
    my_hash = {}
    exep = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    for char in s:
        if char in exep:
            my_word = my_word.replace(char,"")
    words = my_word.split()
    for word in words:
        modified_word = word.lower()
    
        if modified_word in my_hash:
            my_hash[modified_word] += 1
        else:
            my_hash[modified_word] = 1

    return my_hash



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))