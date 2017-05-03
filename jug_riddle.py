"""
Function solving the water jug riddle (see description below) by printing out 
subsequent jug configurations (the amount of water in both jugs).

Water jug riddle:
There are two jugs with fixed (integer) capacities. Neither of the jugs have markings on them.
You need to use these two jugs to measure some exact amount of water to be left in the larger jug. 
"""

import math


def jug(aim, max_cap, min_cap, maxi=0, mini=0):
    """
    Args:
        aim (int): final amount of water to be left in larger jug
        max_cap (int): capacity of larger jug
        min_cap (int): capacity of smaller jug
        maxi (int): current amount of water in larger jug
        mini (int): current amount of water in smaller jug
    """

    # error handling
    if any(x <= 0 for x in (aim, max_cap, min_cap)):
        raise ValueError("Capacity of each jug must be positive.")

    if aim > max_cap:
        raise ValueError("The final amount of water cannot exceed the larger jug's capacity.")

    if aim % math.gcd(max_cap, min_cap) != 0:
        raise ValueError("The final amount of water to be left in the larger jug must be divisible by "
                         "the greatest common divisor of jugs' capacities.")

    def inner_jug(aim, max_cap, min_cap, maxi, mini):
        print(maxi, mini)

        if maxi == aim:
            return

        # if water in smaller jug reaches desired level, pour water out of larger jug
        # and fill it with water from smaller jug
        if mini == aim:
            maxi = mini
            print(maxi, mini)
            return

        while maxi < max_cap:
            mini += min_cap     # fill smaller jug up
            print(maxi, mini)

            am = min(mini, max_cap - maxi)  # amount of water remaining to fill larger jug up
            maxi += am
            print(maxi, mini)

            mini -= am
            print(maxi, mini)

        inner_jug(aim, max_cap, min_cap, mini, 0)

    inner_jug(aim, max_cap, min_cap, maxi, mini)
