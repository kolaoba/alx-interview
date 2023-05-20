#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest 
number of coins needed to meet a given amount total.
"""

from typing import List

def makeChange(coins: List[int], total: int) -> int:
    """
    Returns the fewest number of coins
    needed to meet a given amount total
    """
    counter = 0
    if total <= 0:
        return 0
    sort = sorted(coins, reverse=True)
    for i in range(len(sort)):
        while sort[i] <= total:
            total = total - sort[i]
            counter += 1
    if total == 0:
        return counter
    return -1