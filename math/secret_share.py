"""
created using polynomial interpolation
"""

def f(SECRET,d,points,x):
    poly_to_eval = f"{SECRET}"
    for i in range(d):
        poly_to_eval += f"+ ({points[i]}*({x}**{i+1}))" 
    return eval(poly_to_eval)


SECRET = 109
n = int(input("Min num of numbers needed for the SECRET to be decoded: ")) # min number of persons needed
d = n-1
points = []
for i in range(d) : points.append(int(input("A Random Number: ")))
needed_for = int(input("Number of number a share needed for: "))
for i in range(needed_for):
    print(f" f({i+1}) {f(SECRET,d,points,i+1)}")



