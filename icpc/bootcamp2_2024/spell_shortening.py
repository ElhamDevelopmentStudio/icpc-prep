"""
Spell Shortening

Qasim is attempting to learn magic, but it really hasn't been going very well. In order to pass an upcoming exam, Qasim decides to just memorize magic spells – but even that turns out to be too hard!

A magic spell is, quite simply, a string that consists of only lowercase Latin letters (i.e., the characters {a, b, c, ..., z}).

Qasim has with him a magic spell SS and is struggling to remember it. To make things easier, he decides to delete exactly one character from it – after all, a small modification to the spell won't change its effect, right?

Qasim believes he has a better chance of remembering the spell if it's lexicographically smallest.

Can you help Qasim find which character he should delete so that the resulting string is lexicographically smallest among all possible results?
Note:

Lexicographic order is essentially dictionary order. That is, string AA is lexicographically smaller than string BB if, at the first index where they differ, A[i]<B[i]A[i]<B[i]. For instance, ac is smaller than ad and ba, but not ab.
Input Format:

    The first line of input will contain a single integer TT, denoting the number of test cases.
    Each test case consists of two lines of input:
        The first line of each test case contains a single integer NN, the length of Qasim's spell.
        The second line contains the string SS, representing the spell itself.

Output Format:

For each test case, output on a new line the lexicographically smallest string Qasim can obtain by deleting a single character from SS.
Constraints:

    1≤T≤1051≤T≤105
    2≤N≤3×1052≤N≤3×105
    SS is a length-NN string that contains only lowercase Latin letters.
    The sum of NN across all tests won't exceed 3×1053×105.
"""



def find_smallest_spell(T, test_cases):
    results = []
    for i in range(T):
        N = test_cases[i][0]
        S = test_cases[i][1]
        
        for j in range(N - 1):
            if S[j] > S[j + 1]:
                results.append(S[:j] + S[j+1:])
                break
        else:
            results.append(S[:-1])
    
    return results

T = int(input())  
test_cases = []
for _ in range(T):
    N = int(input())
    S = input()
    test_cases.append((N, S))

output = find_smallest_spell(T, test_cases)

print("\n".join(output))

