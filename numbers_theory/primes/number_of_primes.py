"""
from page 198 of comp prog handbook
to count the number of primes between 1 and n


                      n
num_of_primes(n) = -------
                    log(n)
"""

import math
number_of_primes = lambda n : math.floor(n / math.log(n))

# num_of_primes of 10^6 = 72382

print(number_of_primes(10**6))
print(number_of_primes(10))
