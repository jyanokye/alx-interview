#!/usr/bin/python3

"""makechange function"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    """
    if total <= 0:
        return 0

    # Create a list that stores the minimum number of coins for each total amount from 0 to the given total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Calculate the minimum number of coins needed for each total amount
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    # Returns the fewest number of coins needed for the given total
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
