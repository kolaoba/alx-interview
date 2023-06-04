#!/usr/bin/python3
"""
Determine who the winner of each game is.

input: rounds = x
       array = nums
return: name of the player that won the most rounds
        None if winner cannot be determined
"""


def is_prime(num):
    """
    Check number is prime
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num >= 3:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
    return True


def generate_primes(n):
    """
    Generate a list of prime numbers in array n
    """
    return [p for p in range(2, len(n)) if is_prime(p)]


def find_multiples(value, primes):
    """
    Find multiples of a value in the primes array
    """
    return [num for num in primes if num % value == 0]


def isWinner(x, nums):
    """
    Determine winner
    """
    Maria_wins = 0
    Ben_wins = 0

    while x:
        primes = generate_primes(nums)
        for val in primes:
            if val in nums:
                nums.remove(val)
            multiples = find_multiples(val, nums)
            for mul in multiples:
                nums.remove(mul)
        if len(primes) % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1
        x -= 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    return None
