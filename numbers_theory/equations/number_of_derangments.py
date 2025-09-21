"""
from pag 214 of comp prog 
given a number 'n'
find the number of derangments of their permuatations
derangments here means the perms where every element is not where they are supposed to be

for ex:
    if n = 3 = ideal pos of each elem{1,2,3}
    derang 1 : {2,3,1}
    derang 2 : {3,1,2}
    so if n = 3 then res = 2


        |
        |0      n = 1
        |
        |2      n = 2
f(n) -> |
        |(n-1)(f(n-2) + f(n-1)) n > 2
        |
        |
        |
        |
"""
def main(n):
    if n == 1 : return 0
    if n == 2 : return 1
    if n > 2  : return (n-1)*(main(n-2)+main(n-1))

if __name__ == "__main__":
    res = main(3)
    print(res)
