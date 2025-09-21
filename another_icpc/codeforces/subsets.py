def get_subsets(arr):
    # Base case: if the array is empty, return a list containing the empty set
    if not arr:
        return [[]]
    
    # Recursive case: get all subsets of the array without the first element
    subsets_without_first = get_subsets(arr[1:])
    
    # For each subset without the first element, create a new subset that includes the first element
    subsets_with_first = [[arr[0]] + subset for subset in subsets_without_first]
    
    # Combine the subsets with and without the first element
    return subsets_without_first + subsets_with_first

# Example usage:
arr = list(map(int,input().split()))
subsets = get_subsets(arr)
print(subsets)
