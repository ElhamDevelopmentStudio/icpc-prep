import sys
from io import StringIO



input_string = """7
2 3 1 2
2 3 3 4
2 3 4 5
2 3 2 3
2 3 3 5
2 3 1 10
2 3 10 11
"""


sys.stdin = StringIO(input_string)


result = []

def get_location(s):
    module_of_s = s % 5
    res = 5 if module_of_s == 0 else module_of_s 
    
    if res < 3:
        return "left",res
    else:
        return "right",res

def solve(n,r,s1,s2):
    s1_direction,s1_location = get_location(s1)
    s2_direction,s2_location = get_location(s2)
    

    #print(f"s1_direction=")
    print(f"s1_direction = {s1_direction},s1_location = {s1_location}")
    print(f"s2_direction = {s2_direction},s2_location = {s2_location}\n")
    if s1_direction != s2_direction:
        return "no"

    if (s1_location+1)== s2_location or (s1_location-1)==s2_location:
        return "yes"
    return "no"

for _ in range(int(input())):
    n,r,s1,s2 = list(
        map(int,input().split())
    )

    result.append(
            solve(n,r,s1,s2)
    )
print(
    "\n".join(
            [str(x) for x in result]
        )
)
