def left_bit_shift(x : int , k :int) -> int:
    """x << k equals to x * 2 ^ k

    Args:
        x (int): the first num
        k (int): the second num

    Returns:
        int: returns x * 2 ^ k
    """
    return x << k

def right_bit_shift(x : int,k :int)  ->int:
    """x >> k equals to x / 2 ^ k

    Args:
        x (int): the first num
        k (int): the second num

    Returns:
        int: returns x / 2 ^ k
    """
    return x >> k
    

def bit_shift(x : int, k :int) -> bool:
    """
    A number of the form 1 ˙˙ k has a one bit in position k and all other bits are zero,
    so we can use such numbers to access single bits of numbers. In particular, the
    kth bit of a number is one exactly when x & (1 << k) is not zero

    Args:
        x (int): _description_
        k (int): _description_

    Returns:
        bool: _description_
    """

    return x & 1 << k != 0
if __name__ == "__main__":
    x = 2
    k = 3
    left = left_bit_shift(x,k)
    right = right_bit_shift(x,k)

    print(left)
    print(right)



