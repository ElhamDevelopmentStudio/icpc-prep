def to_minus(x : int) -> int:
    """returns the minus of the number , adding one to will equal to that number but minus

    Args:
        x (int): the number which should be minused

    Returns:
        int: minus of 'x'
    """
    return ~x + 1


if __name__ == "__main__":
    while True:
        this = input()
        if this == "\n" : break
        this = int(this)
        to_min = to_minus(this)
        print(to_min)
