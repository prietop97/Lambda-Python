import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements o(n + k)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ? stretch ? #

# o(n log(k))
names_2.sort() # o(k log(k))

for name_1 in names_1: # o(n log(k))
    high = len(names_2) - 1
    low = 0
    mid = (low + high) // 2
    
    while low <= high:
        mid = (low + high) // 2
        if names_2[mid] == name_1:
            duplicates.append(name_1)
            break
        elif names_2[mid] > name_1:
            high = mid - 1
        elif names_2[mid] < name_1:
            low = mid + 1
        else:
            break
    
# my_hash = {}
# for name_1 in names_1:
#     my_hash[name_1] = True

# for name_2 in names_2:
#     if my_hash.get(name_2):
#         duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
