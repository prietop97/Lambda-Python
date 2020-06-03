# A child is running up a staircase with n steps and can hop either 1 step, 2 step, or 3 steps at a time. Implement a method to count how many possible ways a child can run up the stairs

def triple_set(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return triple_set(n - 1) + triple_set(n - 2) + triple_set(n - 3)


def triple_set_2(n, cache={0:1,1:1}):
    if n < 0:
        return 0
    if n not in cache:
        cache[n] = triple_set_2(n - 1) + triple_set_2(n - 2) + triple_set_2(n - 3)

    return cache[n]


def triple_set_3(n):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1

    for i in range(1,n + 1):
        total = 0
        for j in range(1,4):
            if i - j >= 0:
                total += cache[i - j] 
        cache[i] = total

    return cache[n]

# GIVEN A SET OF POSSIBLE STEPS
def triple_set_4(n,possibles):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1

    for i in range(1,n + 1):
        total = 0
        for possible in possibles:
            if i - possible >= 0:
                total += cache[i - possible] 
        cache[i] = total

    return cache[n]




print(triple_set(5))
print(triple_set_2(5))
print(triple_set_3(5))

print(triple_set_4(5,[1,2,3,5]))
print(triple_set_4(5,[2,3]))
print(triple_set_4(5,[1,2,3,5]))