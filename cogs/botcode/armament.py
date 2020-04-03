import random

def hit_or_miss():
    # Simply, a hit is an even numbered roll.
    die_roll = random.randint(1, 6)
    # print die_roll
    if die_roll % 2:
        return False
    else:
        return True


hit_or_miss()