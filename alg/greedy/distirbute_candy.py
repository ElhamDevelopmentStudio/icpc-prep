"""
'n' kids stand in a line , each having an integer rating.
we distirbute candies following:
    - each kid gets atleast 1 candy
    - kids with higher rating than neighbours get more candies

find the minimum candies required
"""


def solve(arr:list[int]) -> int:
    d = sorted((x,i) for i,x in enumerate(arr))

    candies = [1] * len(arr)

    for _,i in d:
        if i > 0 and arr[i] > arr[i-1]:
            candies[i] = max(candies[i],candies[i-1] + 1)

        if i < len(arr) - 1 and arr[i] > arr[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)

    return sum(candies)


if __name__ == "__main__":
    arr= [1,3,7,1]
    #     1 2 3 1
    res = solve(arr)
    print(res)