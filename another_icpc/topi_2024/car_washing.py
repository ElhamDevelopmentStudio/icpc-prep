import sys
from io import StringIO
from typing import List

input_string = """2
5
2 4
7 9 3 4 8
8 5 6 4 5
2 3 1 3
2 1 2 2
3 2
4
10 12
6 7 8 9
5 6 7 8
4 2 3
2 1 3
3 4
"""

sys.stdin = StringIO(input_string)

def get_list() -> List[int]:
    return list(map(int, input().split()))

def solve(
    num_of_stations,
    lane_1_entry,
    lane_2_entry,
    lane_1_processing,
    lane_2_processing,
    lane_1_switching,
    lane_2_switching,
    lane_1_exit,
    lane_2_exit
) -> int:
    # Initialize DP tables
    dp1 = [0] * num_of_stations
    dp2 = [0] * num_of_stations

    # Base case: Start at entry point
    dp1[0] = lane_1_entry + lane_1_processing[0]
    dp2[0] = lane_2_entry + lane_2_processing[0]

    """
    [9,]
    [12]

    """
    for i in range(1, num_of_stations):
        print(
            f"""\n\n\n
            STEP {i}\n
            lane_1 : {dp1}\n
            lane_2 : {dp2}
            """
        )
        dp1[i] = min(
            dp1[i-1] + lane_1_processing[i],
            dp2[i-1] + lane_2_switching[i-1] + lane_1_processing[i]
        )
        
        dp2[i] = min(
            dp2[i-1] + lane_2_processing[i], 
            dp1[i-1] + lane_1_switching[i-1] + lane_2_processing[i]
        )

    return min(dp1[num_of_stations-1] + lane_1_exit, dp2[num_of_stations-1] + lane_2_exit)

T = int(input())
for _ in range(T):
    num_of_stations = int(input())
    lane_1_entry, lane_2_entry = get_list()
    lane_1_processing = get_list()
    lane_2_processing = get_list()
    lane_1_switching = get_list()
    lane_2_switching = get_list()
    lane_1_exit, lane_2_exit = get_list()

    result = solve(
        num_of_stations=num_of_stations,
        lane_1_entry=lane_1_entry,
        lane_2_entry=lane_2_entry,
        lane_1_processing=lane_1_processing,
        lane_2_processing=lane_2_processing,
        lane_1_switching=lane_1_switching,
        lane_2_switching=lane_2_switching,
        lane_1_exit=lane_1_exit,
        lane_2_exit=lane_2_exit
    )
    print(result)
    exit()




"""
import sys
from io import StringIO
from typing import List


input_string = "2
5
2 4
7 9 3 4 8
8 5 6 4 5
2 3 1 3
2 1 2 2
3 2
4
10 12
6 7 8 9
5 6 7 8
4 2 3
2 1 3
3 4
"

sys.stdin = StringIO(input_string)


def get_list() -> List[int]:
    return list(map(int,input().split()))


def opp_lane(lane : int):
    return 1 if lane == 1 else 0


def debug(msg,*args):
    print(msg)
    for arg in args:
        print(arg)
    print("\n")

def solve(
    *,
    num_of_stations,
    lane_1_entry,
    lane_2_entry,
    lane_1_processing,
    lane_2_processing,
    lane_1_switching,
    lane_2_switching,
    lane_1_exit,
    lane_2_exit
) -> int:
    result = []
    if lane_1_entry < lane_2_entry:
        lane = 1
    else:
        lane = 2
    
    #print(f"we goin with lane {lane}")
    result.append(
        lane_1_entry if lane == 1 else lane_2_entry
    )
    print(*lane_1_processing)
    print(*lane_2_processing)
   

    print(*lane_1_switching)
    print(*lane_2_switching)
    

    for i in range(num_of_statios):
        result.append(
            lane_1_processing[i] if lane == 1 else lane_2_processing[i]
        )

        if i == num_of_statios-1:
            continue
        if lane == 1:
            if lane_1_processing[i] == 4:
                debug(
                    "lane when 4",
                    lane_1_switching[i],
                    lane_2_processing[i+1],
                    lane_1_processing[i+1]
                )
            if lane_1_switching[i] + lane_2_processing[i+1] < lane_1_processing[i+1]:
                result.append(
                    lane_1_switching[i]
                )
                lane = 2
        else:
            if lane_2_switching[i] + lane_1_processing[i+1] < lane_2_processing[i+1]:
                result.append(
                    lane_2_switching[i]
                )
                lane = 1
        

    result.append(
        lane_1_exit if lane ==1 else lane_2_exit
    )
    print(*result)
    return sum(result)

for _ in range(int(input())):
    num_of_statios = int(input())
    
    lane_1_entry,lane_2_entry = get_list()
    
    lane_1_processing = get_list()
    
    lane_2_processing = get_list()

    lane_1_switching = get_list()

    lane_2_switching = get_list()

    lane_1_exit,lane_2_exit = get_list()

    
    result = solve(
        num_of_stations=num_of_statios,
        lane_1_entry=lane_1_entry,
        lane_2_entry=lane_2_entry,
        lane_1_processing=lane_1_processing,
        lane_2_processing=lane_2_processing,
        lane_1_switching=lane_1_switching,
        lane_2_switching=lane_2_switching,
        lane_1_exit=lane_1_exit,
        lane_2_exit=lane_2_exit
    )
    print(result)
"""
