"""
hassan is happy if the number is in his range otherwise he is not 
count his most and min happiness

input :
4 1 3
4 3 2 1
output:
2 -1

Explanation:
4 (length of arr) 1(min love of hassan) 3(most love)
4 3 2 1 -> arr to check the numbers in
"""



for _ in range(int(input())):
    length,min_range,max_range = list(map(int,input().split()))
    _range = range(min_range,max_range+1)
    nums = list(map(int,input().split()))
    happines = 0
    max_love = 0
    min_love = 0
    for num in nums:
        if num in _range:
            happines+=1
            max_love = max(happines,max_love) 
        else:
            happines -= 1
            min_love = min(min_love,happines)

    print(max_love,min_love)
