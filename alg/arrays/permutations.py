from itertools import permutations


arr = [1,2,3,4,5]
this = permutations(arr,len(arr))

print(len(list(this)))
# for perm in this:
#     print(perm)
