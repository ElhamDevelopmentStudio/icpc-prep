import collections


def is_even(num : int) -> bool:
    return num & 1 == 0

def is_odd(num : int) -> bool:
    return num & 1 == 1


def is_divisible_by_k(x:int ,k : int) -> bool:
    return x & ( (2 ** k ) - 1 ) == 0


if __name__ == "__main__":
    assert is_even(3) == False
    assert is_odd(10) == False
    assert is_divisible_by_k(8,3) == True
