# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/12/2023
# Description: Write a recursive function named row_puzzle that takes
# a list of integers (the row) as a parameter and returns True if the
# puzzle is solvable for that row, but returns False otherwise.

def row_puzzle_pos(row, spot, visited):
    """Returns whether the current position is zero."""
    if row[spot] == 0:
        possible = True
    else:
        visited = visited[:]  # Results in False if the position has already been visited.
        if visited[spot]:
            possible = False
        else:
            visited[spot] = True
            possible = False
            if spot - row[spot] > 0 and row_puzzle_pos(row, spot - row[spot], visited):
                return True  # moves to the left, if possible.
            if spot + row[spot] < len(row) and row_puzzle_pos(row, spot + row[spot], visited):
                return True  # moves to the right, if possible.
    return possible


def row_puzzle(row):
    """Returns whether each integer was visited."""
    visited = [False for int in range(len(row))]
    return row_puzzle_pos(row, 0, visited)  # int is set to zero.

# move = row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0])
# print(move)
# move = row_puzzle([1, 3, 2, 1, 3, 4, 0])
# print(move)
