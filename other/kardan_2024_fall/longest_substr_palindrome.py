def is_pal(w):
    l = 0
    r = len(w) - 1 
    while l < r:
        if w[l] != w[r]:
            return False
        l += 1
        r -= 1
    return True


def longest_pal_substr(word):
    longest = 0
    longest_word = ""
    for i in range(len(word)):
        for j in range(i,len(word)):
            w = word[i:j+1]
            if (w == w[::-1]) and len(w) > longest:
                longest = len(w)
                longest_word = w

    
    print(longest_word)
    return longest

def generate_substr(word):
    output = []
    n = len(word)
    for i in range(1 << n):
        local_output = "" 
        for j in range(n):
            if i & (1 << j):
                local_output += word[j]
        output.append(local_output)
    
    longest_word = ""
    longest = float("-inf")
    for w in output:
        len_w = len(w)
        #print(w)
        if len_w == 0:
            continue
        elif len_w == 1 and len_w > longest:
            longest = len_w
            longest_word = w

        elif  is_pal(w) and longest < len_w :
            longest = len_w
            longest_word = w

    return longest_word
            



wow = "abc"

word = "forgeeksskeegfor" #geeksskeeg
print(generate_substr(word))

#print(
#    longest_pal_substr(word)
#)
