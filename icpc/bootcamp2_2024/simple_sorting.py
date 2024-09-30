"""
given chars or number,floats as input sort them

input : 
1 1.2 0.8 8.0 8 8.1
output :
0.8 1 1.2 8.0 8 8.1


input :
c b a
a b a
"""

def get_type(
    n : str
) -> str:
    if n[0].isalpha():
        return "str"
    elif "." in n:
        return "float"
    else:
        return "digit"

for _ in range(int(input())):
    inputs = list(map(str,input().split()))
    mein_arr = []

    for word in inputs:
        this_word_type = get_type(word)
        if this_word_type == "digit":
            mein_arr.append(
                ("digit",float(word),word)
            )
        elif this_word_type == "float": 
            mein_arr.append(
            ("float",float(word),word)
        )
        else:
            mein_arr.append(
                ("str",word,word)
            )


    sorted_arr = sorted(mein_arr,key=lambda x: x[1])
    
    result = []
    
    for w in sorted_arr:
        result.append(w[2])

    print(*result)


