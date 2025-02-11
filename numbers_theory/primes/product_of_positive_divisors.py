from collections import defaultdict
import math

def prime_factors(n):
    """Find the prime factors of a number and their powers."""
    factors = defaultdict(int)
    
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    
    # Check for odd factors from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    
    # If n is still greater than 2, it must be a prime number
    if n > 2:
        factors[n] += 1
    
    return factors

def generate_divisors(factors):
    """Generate all divisors from the prime factorization."""
    primes = list(factors.keys())
    exponents = [0] * len(primes)
    divisors = []
    
    while True:
        # Calculate the current divisor
        divisor = 1
        for i in range(len(primes)):
            divisor *= primes[i] ** exponents[i]
        divisors.append(divisor)
        
        # Increment exponents like an odometer
        for i in range(len(exponents)):
            exponents[i] += 1
            if exponents[i] <= factors[primes[i]]:
                break
            exponents[i] = 0
        else:
            # All combinations have been generated
            break
    
    return sorted(divisors)

def number_of_divisors_and_list(n):
    """Find the number of divisors and list them."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Step 1: Prime factorization
    factors = prime_factors(n)
    
    # Step 2: Calculate the number of divisors
    num_divisors = 1
    for exponent in factors.values():
        num_divisors *= (exponent + 1)
    
    # Step 3: Generate the list of divisors
    divisors = generate_divisors(factors)
        
    # Print results
    print(f"Number of divisors: {num_divisors}")
    print(f"Divisors: {divisors}")

    return divisors
# Example usage
number = int(input("Enter a number: "))
divisor =  number_of_divisors_and_list(number)
print(number ** (len(divisor)//2))
