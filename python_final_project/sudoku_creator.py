base = 3
side = base * base


# pattern for a baseline valid solution
def pattern(r, c): return (base * (r % base) + r // base + c) % side


# randomize rows, columns and numbers (of valid base pattern)
from random import sample


def shuffle(s): return sample(s, len(s))


def create_board():
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    return board

print(create_board())