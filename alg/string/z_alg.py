"""
from page 250 of comp prog handbook
and also : https://www.youtube.com/watch?v=Tg1w-0a1xew
"""
def calc_z_arr(s):
    n = len(s)
    # the main z_arr
    z = [0] * n
    
    # l for left handler , r for right handler , and k for helper when it is in box
    l,r,k = 0,0,0
    
    for i in range(1,n):
        # if i is bigger than r than it means we are outside the box
        # the solution is naive way of finding what to do with this number
        if i > r:
            # update the left,right to the curr 
            l,r = i,i
            # until we are out of bounds and the curr postions equals the the start of substr
            while r < n and s[r] == s[r-l]:
                r+=1
            # this z value of the curr index is the value of the box
            z[i] = r-l
            # idk why we do this but we do
            r-=1
        # if i isnt bigger than we are in the box
        else:
            # put the k into i - l meaning into the corrosponding realtive value of i outside box
            k = i-l
            """
            if z[k] , meaning that past relative number is:
            smaller than r-i+1 : we can copy numbers
            if equal or bigger : we should count again
            """
            if z[k] < r -i +1:
                z[i] = z[k]

            else:
                # dont forget to update the l to curr , since this count as a new z box
                l = i
                while r < n and s[r] == s[r-l]:
                    r+=1
                z[i] = r-l
                r-=1
    return z


def z_alg(pattern,word):
    """
    one of the main ways z_alg is used , is to count the number of times
    a pattern has happend in a string 
    of course this can be done easily in O(n^2) using 2 for loops
    but using z_alg we can do it in n+m where n is the pattern and m is string
    """
        
    # we add a custom sybmol so the the prefix always matches the pattern
    len_pattern = len(pattern)
    combined = pattern + "#" + word
    print(combined)
    z_arr = calc_z_arr(combined)
    print(*z_arr)
    result = []
    number_of_patterns = 0

    for i in range(len(z_arr)):
        if z_arr[i] == len_pattern:
            number_of_patterns += 1
            # if we want the starting index of the substr , then we can deduct the len of the substr from length_of_pattern - 1
            result.append(i - len_pattern - 1)
    return result,number_of_patterns


if __name__ == "__main__":
    arr = ['A','C','B','A','C','D','A','C','B','A','C','B','A','C','D','A']
    pattern = "ACB"
    z_array = calc_z_arr(arr)
    print(*z_array)
    #indexes , number_of_patterns = z_alg(pattern,"".join(arr))
    #print(*indexes)
    #print(number_of_patterns)
    



