def is_prime(num):
    for i in range(2,num // 2):
        if num % i == 0:
             return False
    return True

print(is_prime(6))