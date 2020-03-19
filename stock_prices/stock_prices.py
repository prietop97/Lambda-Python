#!/usr/bin/python

import argparse

## GO THROUGH EACH PRICE
## GO THROUGH THE REST OF THE PRICES TO THE RIGHT
## TEMP VARIABLE FOR NEXT PRICE - CURRENT PRICE IF NEXT_PRICE - CURRENT PRICE > TEMP VARIABLE
## CHANGE CURRENT PRICE TO THE TEMP 
## FIND THE MAX  

# def find_max_profit(prices):
#   profits = [float('-inf')] * len(prices) ## CAN BE DONE IN 0(1) BUT THAT WOULD MUTATE THE CURRENT PRICES ARRAY WHICH IS NOT IDEAL IN A REAL WORLD APPLICATION

#   for i in range(len(prices)):

#     for j in range(i + 1,len(prices)):
      
#       if prices[j] - prices[i] > profits[i]:
#         profits[i] = prices[j] - prices[i]

#   return max(profits)


## BETTER IMPLEMENTATION
def find_max_profit(prices):
  if not prices:
    return 0

  max_profit = float("-inf")
  minimum = prices[0]

  for i in range(1,len(prices)):
    if prices[i] - minimum > max_profit:
      max_profit = prices[i] - minimum
    if prices[i] < minimum:
      minimum = prices[i]

  return max_profit

print(find_max_profit([10000, 1000, 5900, 50, 5000, 10]))
print(find_max_profit([]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))