def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the KMP algorithm.
    
    Parameters:
    pattern (str): The pattern string to process
    
    Returns:
    list: LPS array where lps[i] is the length of the longest proper prefix 
        which is also a suffix of pattern[0..i]
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Search for all occurrences of a pattern in a text using the KMP algorithm.
    
    Parameters:
    text (str): The text to search in
    pattern (str): The pattern to search for
    
    Returns:
    list: List of starting indices where the pattern occurs in the text
    
    Raises:
    ValueError: If pattern is empty
    """
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    indices = []
    
    i = j = 0  # i for text index, j for pattern index
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices

if __name__ == "__main__":
    # Example usage
    text = "ABABACABABCABABACABAB"
    pattern = "ABAB"
    try:
        print(f"Text: {text}")
        print(f"Pattern: {pattern}")
        matches = kmp_search(text, pattern)
        print("Pattern found at indices:", matches)
    except ValueError as e:
        print(e)

