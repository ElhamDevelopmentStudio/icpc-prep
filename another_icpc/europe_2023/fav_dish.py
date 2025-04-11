from collections import defaultdict
import sys
from io import StringIO


input_string = """4 3
2 5
3 4
4 2
1 6
6 4
2 8
5 5
"""


sys.stdin = StringIO(input_string)


N,M = list(map(int,input().split()))


dishes = []

for i in range(N):
    dishes.append(
        list(map(int,input().split()))
    )


persons = []
for i in range(M):
    persons.append(
        list(map(int,input().split()))
    )

result = []


def calc_result(person,dish):
    person_taste,person_plate = person
    dish_taste , dish_plate = dish

    upper = (person_taste * dish_taste) + (person_plate * dish_plate) 
    lower = person_plate + person_taste
    return upper /lower 


for person in persons:
    local_res = []
    seen_amount = defaultdict(int) 
    max_amount = float("-inf")
    for dish in dishes:
        this_res = str(calc_result(person,dish))
        local_res.append(
                this_res 
        )
        seen_amount[this_res] += 1
        if seen_amount[this_res] > max_amount:
            max_amount = seen_amount[this_res]
    print(*local_res)
    print(*set(local_res))
    result.append(max_amount)

print(
    "\n".join(
        [str(x) for x in result]
    )
)
