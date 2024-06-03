"""

from page 235 of comp prog handbook
2 player play , and on each turn u can either remove 1 , 2 , 3 from total sticks
whoever removes the last stick wins the game

"""

def solve(num_of_sticks : int) -> bool:
    return num_of_sticks % 4 != 0

if __name__ == "__main__":
    num_of_sticks = 10
    res = solve(num_of_sticks)
    print(res)
