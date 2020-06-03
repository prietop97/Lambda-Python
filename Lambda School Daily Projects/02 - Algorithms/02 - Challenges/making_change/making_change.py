#!/usr/bin/python

import sys


def making_change(amount, denominations):
  db = [0 for i in range(amount + 1)]
  db[0] = 1

  for coin in denominations:
    for j in range(coin,amount + 1):
      db[j] += db[j - coin]

  return db[amount]

print(making_change(5,[1,5]))
  




# 1 - 1
# 2 - 1 1
# 3 - 1 1 1
# 4 - 1 1 1 1
# 5 - 1 1 1 1 1
#   - 5
# 6 - 1 1 1 1 1 1
#   - 5 1
# 7 - 1 1 1 1 1 1 1
#   - 5 1 1
# 8 - 1 1 1 1 1 1 1 1
#   - 5 1 1 1
# 9 - 1 1 1 1 1 1 1 1 1
#   - 5 1 1 1 1
# 10 - 1 1 1 1 1 1 1 1 1
#    - 5 5
#    - 5 1 1 1 1 1
#    - 10
# 11 - 1 1 1 1 1 1 1 1 1 1
#    - 5 5 1
#    - 5 1 1 1 1 1 1
#    - 10 1
# 15 - 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#    - 5 5 5
#    - 5 5 1 1 1 1 1
#    - 10 5
#    - 10 1 1 1 1 1
#    - 5 1 1 1 1 1 1 1 1 1 1


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")