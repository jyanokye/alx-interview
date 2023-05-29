#!/usr/bin/python3
"""Winner is prime"""


def isWinner(x, nums):
    """
    Determines the winner between two players, Maria and Ben, based on a list of numbers.

    Args:
        x: Unused argument.
        nums (list): A list of numbers.

    Returns:
        str or None: The name of the winner ("Maria" or "Ben"), or None in case of a tie.

    """
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        is_maria_turn = True
        while n > 1:
            prime = 2
            while n % prime != 0:
                prime += 1

            if is_maria_turn:
                is_maria_turn = False
                wins["Ben"] += 1  # Increment Ben's wins instead of Maria's
            else:
                is_maria_turn = True
                wins["Maria"] += 1  # Increment Maria's wins instead of Ben's

            while n % prime == 0:
                n //= prime

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
