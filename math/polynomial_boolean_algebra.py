"""

we can use polynomical expressions to express boolean algebra

for ex:
    AND -> f(x,y) = x*y
    NOT -> f(x) = 1-x
    OR  -> f(x,y) = 1 - (1-x)*(1-y)

"""

AND = lambda x,y : x*y
OR = lambda x,y : 1-(1-x)*(1-y) # or NOT(NOT(x)*NOT(y))
NOT = lambda x : 1-x 


