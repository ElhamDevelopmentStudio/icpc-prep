def lagrange_interpolation(x, x_s, y_s):
    """
    Given n points (x_s, y_s), this function uses Lagrange interpolation
    to find the polynomial that goes through these points and evaluates
    it at x.
    """
    def basis(j):
        p = [(x - x_s[m]) / (x_s[j] - x_s[m]) for m in range(len(x_s)) if m != j]
        return functools.reduce(lambda x, y: x * y, p)

    return sum(y_s[j] * basis(j) for j in range(len(x_s)))

def reconstruct_secret(points):
    """
    Given a list of points, this function uses Lagrange interpolation
    to reconstruct the secret.
    """
    x_s = [point[0] for point in points]
    y_s = [point[1] for point in points]
    
    # The secret is the value of the polynomial at x = 0
    secret = lagrange_interpolation(0, x_s, y_s)
    return secret


"""
created using polynomial interpolation
"""

def f(SECRET,d,points,x):
    poly_to_eval = f"{SECRET}"
    for i in range(d):
        poly_to_eval += f"+ ({points[i]}*({x}**{i+1}))" 
    return eval(poly_to_eval)



# Example usage
SECRET = 109
n = int(input("Min num of numbers needed for the SECRET to be decoded: "))  # min number of persons needed
d = n - 1
points = []
for i in range(d):
    points.append(int(input("A Random Number: ")))
needed_for = int(input("Number of number a share needed for: "))
shares = []
for i in range(needed_for):
    x = i + 1
    y = f(SECRET, d, points, x)
    shares.append((x, y))
    print(f" f({x}) = {y}")

# Reconstruct the secret from the shares
secret_points = shares[:n]  # Use the first n shares to reconstruct the secret
reconstructed_secret = reconstruct_secret(secret_points)
print(f"Reconstructed Secret: {reconstructed_secret}")

