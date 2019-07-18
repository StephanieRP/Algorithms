#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_num = prices[1] - prices[0]  # subtracts first 2 prices
       for i in range(0, len(prices)):  # loop through sale prices
            buy = prices[i]  # define the buying value
            for j in range(i + 1, len(prices)):  # loop through the prices comparing buy value
                profit = prices[j] - buy
                if profit > max_num:
                    max_num = profit
        return max_num

        find_max_profit([1050, 270, 1540, 3800, 2]) # testing


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
