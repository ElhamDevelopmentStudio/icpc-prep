"""

the division theorom says that for any integer a and positive integer b,there exists one pair of integers q and r such that

```
a = bq + r
```

where 0 <= r < b.

a = dividend
b = divisor
q = quotient
r = remainder


r=1
b=6
a=?
q=?

a=b*q+r
a=6q+1


"""


def division_algorithm(
    *,
    b : int,
    q : int,
    r : int
) -> int:
    a= b*q+r
    return a


