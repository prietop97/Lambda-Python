#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#   if n <= 1:
#     return 3
#   return 3 * rock_paper_scissors(n - 1)


def rock_paper_scissors(n):
    total = []
    moves = ["rock", "paper", "scissors"]

    def rock_paper_scissors_recurse(plays, n):
        if n == 0:
            total.append(plays)
            return
        rock_paper_scissors_recurse(plays + [moves[0]], n - 1)
        rock_paper_scissors_recurse(plays + [moves[1]], n - 1)
        rock_paper_scissors_recurse(plays + [moves[2]], n - 1)

    rock_paper_scissors_recurse([], n)

    return total

print(rock_paper_scissors(100))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

