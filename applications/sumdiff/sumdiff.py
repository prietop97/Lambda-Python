"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


# def f(x):
#     return x * 4 + 6

# cache_left = {}
# cache_right = {}
# def get_per(tuplee):
#     for num in tuplee:
#         for num2 in tuplee:
#             if num != num2:
#                 num11 = f(num)
#                 num22 = f(num2)
#                 if ((num11, num22) or (num22,num11)) not in cache_left:
#                     cache_left[num11,num22] =  
