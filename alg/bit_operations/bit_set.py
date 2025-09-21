max_num = 31
subset_to_be_presented = [1,2,3,4,8]

set_ = 0
for num in subset_to_be_presented:
    set_ |= (1<<num)


for i in range(max_num):
    if set_ & (1<<i): print(i)
print(bin(set_)[2:])
print(set_.bit_count())
