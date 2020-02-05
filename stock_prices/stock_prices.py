#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  price_copy = prices[:]
  price_copy.sort()
  if prices == price_copy:
    max_profit = prices[-1] - prices[0]
  elif prices[::-1] == price_copy:
    max_profit = prices[-1] - prices[-2]
  else:
    for i in range(len(prices)-1):
      subset = prices[i:]
      subset.sort()
      if subset[-1] - prices[i] > max_profit:
        max_profit = subset[-1] - prices[i]
  return max_profit

  #go through and find the minimum value, before the last item
  #go through and find the maximum value, after the min value
  #subtract the second from the first which is the profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))