# this = [1,3,4,5,6]

# my_set = set(this)

# i = 0
# l = len(my_set)

# my_iter = iter(my_set)


# while i < l:
#     print(next(my_iter))
#     i += 1

# first = [1,2,3,4,5]
# second = [5,6,7,8,9]
# set_1 = set(first)
# set_2 = set(second)

# combined = set_1 | set_2
# print(type(combined))
# print(combined)

a = [5,2,8,9,4]
b = [3,2,9,5]

set_a = set(a)
set_b = set(b)

combined_a_b = set_a & set_b

print(combined_a_b)
print(len(combined_a_b))