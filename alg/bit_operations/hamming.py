def hamming(a: str, b: str) -> int:
    a_, b_ = int(a, 2), int(b, 2)
    this = a_ ^ b_
    return this.bit_count()


a = "01101"
b = "11001"
res = hamming(a, b)
print(res)
