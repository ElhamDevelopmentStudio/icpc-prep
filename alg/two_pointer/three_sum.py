def solve(nums : list[int], target:int) -> list[list[int]]:
    # O(n^2)
    nums.sort() # O(logn)
    ans = []
    for i in range(0,len(nums) - 2):# O(n)
        l = i+ 1
        r = len(nums) - 1 
        while l<r: # O(n)
            this = nums[i] + nums[l] + nums[r]
            if this == target:
                if this not in ans : ans.append([nums[i],nums[l],nums[r]])
                l += 1
                r-=1
            elif this < target:
                l += 1
            elif this > target:
                r-=1
    return ans


if __name__ ==  "__main__":
    nums = [-1,0,1,2,-1,-4]
    target = 0
    res = solve(nums,target)
    expected =[[-1,-1,2],[-1,0,1]]
    assert res == expected , f"Wrong answer got {res} expected {expected}"
    print(res)